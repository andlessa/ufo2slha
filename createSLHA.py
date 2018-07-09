#!/usr/bin/env python

#Uses an input SLHA file to compute cross-sections using MadGraph and the UFO model files
#The calculation goes through the following steps
# 1) Run MadGraph using the options set in the input file 
# (the proc_card.dat, parameter_card.dat and run_card.dat...).
# Madgraph is used to compute the widths and cross-sections
# 2) Run slhaCreator to extract the information of the MadGraph output
# and generate a SLHA file containing the cross-sections

#First tell the system where to find the modules:
import sys,os
from configParserWrapper import ConfigParserExt
import logging,shutil
import subprocess
import tempfile
import time,datetime
import itertools
import multiprocessing
from collections import OrderedDict
import gzip,imp

FORMAT = '%(levelname)s in %(module)s.%(funcName)s() in %(lineno)s: %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


def getParticlesFromUFO(ufoFolder):
    """
    Uses the information in the UFO file to collect the all the particle objects.
    Returns a list of particle objects containing information about each particle
    in the model.
    
    :param ufoFolder: path to the UFO folder
    :return: List of Particle objects with the particles in the model
    """    
        
    sys.path.append(ufoFolder)
    mod = imp.load_source('particles',os.path.join(ufoFolder,'particles.py'))
    imp.load_source('particles',ufoFolder)
    allParticles = []
    for objStr in dir(mod):
        obj = getattr(mod,objStr)
        if 'Particle' in str(type(obj)):
            allParticles.append(obj)    
    
    return allParticles


def getProcessString(finalStates,initialStates = ['p','p']):
    """
    Generate a process string (e.g. p p > finalStates) given
    the list of final and initial states.
    
    :param finalStates: list of final state strings or PDGs (e.g. ['Z', 'Z'] or [23,23)
    :param initialStates: list of final state strings (e.g. ['p', 'p'])
    
    :return: Process string (e.g. p p > Z Z or p p > 23 23)
    """
    
    pStr = ' '.join(initialStates) + ' > ' + ' '.join([str(fs) for fs in finalStates])    
    return pStr

def defineProcesses(xsecPDGList,ufoFolder,initialStates=['p','p']):
    """
    Given a list of PDGs, generates all process strings with pair of final
    states including these particles. Automatically includes the charge conjugation particles,
    if the anti-particle exists in the model.
    
    :param xsecPDGList: list of PDGs of final states particles (e.g. [PDG1,PDG2,...])
    :param ufoFolder: path to the UFO folder.
    
    :return: list of process strings (e.g. ['p p > PDG1 PDG1', 'p p > PDG1 -PDG1', 'p p > -PDG1 -PDG1', 'p p > PDG1 PDG2',...]) 
    """
    
    #First collect all PDGs appearing in the model (including anti-particles):
    particles = getParticlesFromUFO(ufoFolder)
    modelPDGs = [particle.pdg_code for particle in particles]
    modelPDGs += [-particle.pdg_code for particle in particles if particle.name != particle.antiname]
    #Now select the subset (including anti-particles) of PDGs defined in input:
    finalStates = []
    for pdg in xsecPDGList:
        if pdg in modelPDGs:
            finalStates.append(pdg)
        if -pdg in modelPDGs:
            finalStates.append(-pdg)
        if (not pdg in modelPDGs) and (not -pdg in modelPDGs):
            logger.info('Particle PDG %i not found in model and will be ignored.' %pdg)            
    finalStates = list(set(finalStates))
    twoBodyFS = itertools.product(finalStates,finalStates)
    processes = []
    for fs in twoBodyFS:
        fs = sorted(fs)
        proc = getProcessString(fs, initialStates)
        if not proc in processes:
            processes.append(proc) 
    
    return processes

def getProcessCard(parser):
    """
    Create a process card using the user defined input.
    If a proccard has been defined and it already exists, it will use it instead.
    
    :param parser: ConfigParser object with all the parameters needed
    
    :return: The path to the process card
    
    """
    
    pars = parser.toDict(raw=False)["MadGraphPars"]
    
    if 'proccard'in pars:
        processCard = pars['proccard']     
        if os.path.isfile(processCard):
            logger.debug('Process card found.')
            #Make sure the output folder defined in processCard matches the one defined in processFolder:
            pcF = open(processCard,'r')
            cardLines = pcF.readlines()
            pcF.close()
            outFolder = [l for l in cardLines if 'output' in l and 'output' == l.strip()[:6]]            
            if outFolder:
                outFolder = outFolder[0]
                outFolder = outFolder.split('output')[1].replace('\n','').strip()
                outFolder = os.path.abspath(outFolder)
                if outFolder != os.path.abspath(pars['processFolder'].strip()):
                    logger.debug("Folder defined in process card does not match the one defined in processFolder. Will use the latter.")
                pcF = open(processCard,'w')
                for l in cardLines:
                    if (not 'output' in l) or (not 'output' == l.strip()[:6]):
                        pcF.write(l)
                    else:
                        pcF.write('output %s \n' %os.path.abspath(pars['processFolder']))
                pcF.close()
            if not outFolder:
                pcF = open(processCard,'a')
                pcF.write('output %s \n' %os.path.abspath(pars['processFolder']))
                
            return processCard
        
    else:
        processCard = tempfile.mkstemp(suffix='.dat', prefix='processCard_', 
                                   dir=pars['MG5path'])
        os.close(processCard[0])
        processCard = processCard[1]
        
    processCardF = open(processCard,'w')
    processCardF.write('import model sm \n')
    processCardF.write('define p = g u c d s u~ c~ d~ s~ \n')
    processCardF.write('import model %s \n' %os.path.abspath(parser.getvalue('options','modelFolder')))     
    xsecPDGList = parser.getvalue('options','computeXsecsFor')
    ufoFolder =  parser.getvalue('options','modelFolder')
    processes = defineProcesses(xsecPDGList, ufoFolder)
    for iproc,proc in enumerate(processes):
        processCardF.write('add process %s @ %i \n' %(proc,iproc))
    
    l = 'output %s\n' %os.path.abspath(pars['processFolder'])
    processCardF.write(l)
    processCardF.write('quit\n')
    processCardF.close()
    
    return processCard

def generateProcesses(parser):
    """
    Runs the madgraph process generation.
    This step just need to be performed once for a given
    model and set of processes, since it is independent of the 
    numerical values of the model parameters.
    
    :param parser: ConfigParser object with all the parameters needed
    
    :return: True if successful. Otherwise False.
    """
    
    
    #Get process card:
    processCard = os.path.abspath(getProcessCard(parser))
    pars = parser.toDict(raw=False)["MadGraphPars"]
    
    #Generate process
    logger.info('Generating process using %s' %processCard)
    run = subprocess.Popen('./bin/mg5_aMC -f %s' %processCard,shell=True,
                                stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                                cwd=pars['MG5path'])
         
    output,errorMsg = run.communicate()
    logger.debug('MG5 process error:\n %s \n' %errorMsg)
    logger.debug('MG5 process output:\n %s \n' %output)
    logger.info("Finished process generation")
        
    return True

def generateEvents(parser):
    
    """
    Runs the madgraph process generation.
    This step just need to be performed once for a given
    model and set of processes, since it is independent of the 
    numerical values of the model parameters.
    
    :param parser: ConfigParser object with all the parameters needed
    
    :return: True if successful. Otherwise False.
    """
    
    pars = parser.toDict(raw=False)["MadGraphPars"]
    ncpu = max(1,parser.getvalue("MadGraphPars","ncores"))
    
    processFolder = pars['processFolder']
    outputFolder = pars['mg5out']
    if not os.path.isdir(processFolder):
        logger.error('Process folder %s not found. Maybe something went wrong with the process generation?' %processFolder)
        return False
    else:
        if os.path.isdir(outputFolder):
            logger.info('outputFolder %s found. It will be replaced' %outputFolder)
            shutil.rmtree(outputFolder)
            
        shutil.copytree(processFolder,outputFolder)
        if 'runcard' in pars and os.path.isfile(pars['runcard']):    
            shutil.copyfile(pars['runcard'],os.path.join(outputFolder,'Cards/run_card.dat'))
        if 'paramcard' in pars and os.path.isfile(pars['paramcard']):
            shutil.copyfile(pars['paramcard'],os.path.join(outputFolder,'Cards/param_card.dat'))    
         
            
    #Generate commands file:       
    commandsFile = tempfile.mkstemp(suffix='.txt', prefix='MG5_commands_', dir=outputFolder)
    os.close(commandsFile[0])
    commandsFileF = open(commandsFile[1],'w')
    commandsFileF.write('done\n')
    comms = parser.toDict(raw=False)["MadGraphSet"]
    #Set a low number of events, since it does not affect the total cross-section value
    #(can be overridden by the user, if the user defines a different number in the input card)
    commandsFileF.write('set nevents 10 \n') 
    for key,val in comms.items():
        commandsFileF.write('set %s %s\n' %(key,val))


    if parser.has_option('options','computeWidths'):
        computeWidths = parser.getvalue('options','computeWidths')
        if computeWidths:
            if isinstance(computeWidths,str) or isinstance(computeWidths,unicode):
                commandsFileF.write('compute_widths %s\n' %str(computeWidths))
            else:
                commandsFileF.write('compute_widths all \n')

    #Done setting up options
    commandsFileF.write('done\n')

    commandsFileF.close()
    commandsFile = commandsFile[1]      
    
    logger.info("Generating MG5 events with command file %s" %commandsFile)
    logger.info("Generating MG5 events")
    run = subprocess.Popen('./bin/generate_events --multicore --nb_core=%s < %s' %(ncpu,commandsFile),
                           shell=True,stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,cwd=outputFolder)
      
    output,errorMsg= run.communicate()
    logger.debug('MG5 event error:\n %s \n' %errorMsg)
    logger.debug('MG5 event output:\n %s \n' %output)
      
    logger.info("Finished event generation")
    
    return True
    


def Run_MG5(parser):
    """
    Runs MadGraph5 using the parameters given in parser
   
    :param parser: ConfigParser object with all the parameters needed
    """
    
    pars = parser.toDict(raw=False)["MadGraphPars"]
 
    #Expand relative paths:    
    pars['mg5out'] = os.path.abspath(os.path.expanduser(pars['mg5out']))
    pars['mg5path'] = os.path.abspath(os.path.expanduser(pars['MG5path']))
    pars['processFolder'] = os.path.abspath(os.path.expanduser(pars['processFolder']))
    
    #Checks        
    if not os.path.isdir(pars['MG5path']):
        logger.error("MadGraph folder %s not found" %pars['MG5path'])
        return False
    elif not os.path.isfile(os.path.join(pars['MG5path'],'bin/mg5_aMC')):
        logger.error("MadGraph binary not found in %s/bin" %pars['mg5path'])
        return False
    
    #Run process generation (if required)
    if os.path.isdir(pars['processFolder']):
        logger.info('Process folder found. Will skip the process generation')
    else:
        generateProcesses(parser)      
        
    #Finally generate events and compute widths:
    generateEvents(parser)
    
    return True
   

def getSLHAFile(parser):
    """
    Uses the LHE file generated by MadGraph
    to generate an SLHA file which includes the XSECTION blocks.
    
    :param parser: ConfigParser object with all the parameters needed    
    
    :return: Path to the slha file
    """
    
    pars = parser.toDict(raw=False)["slhaCreator"]
    
    #Use MadGraph banner reader:
    madgraphPath = parser.getvalue('MadGraphPars','MG5path')
    sys.path.append(madgraphPath)
    from madgraph.various.banner import Banner
    
    slhaFile = pars['slhaout']
    #Create output dirs, if do not exist:
    try:
        os.makedirs(os.path.dirname(pars['slhaout']))
    except:
        pass
    
    lheFile = parser.getvalue('slhaCreator','inputFile')
    
    if not os.path.isfile(lheFile):
        logger.error("File %s not found" %lheFile)
        return False
    
    if lheFile[-3:] == '.gz':
        f = gzip.open(lheFile, 'r')
    else: 
        f = open(lheFile,'r')
    banner = Banner()
    banner.read_banner(f)
    f.close()
    #Check if input file is MG5 banner or SLHA file
    if not 'mggenerationinfo' in banner or not 'mg5proccard' in banner or not 'init' in banner or not 'slha' in banner:
        logger.error("Input file %s does not contain required data " %lheFile)
        return False
       
    #Collect necessary info:
    slhaData = banner['slha']    
    
    #Get generated processes:
    finalStatesDict = {}
    for l in banner['mg5proccard'].split('\n'):
        if not l or l[0] == '#':
            continue
        l = l.strip()
        if l[:8] == 'generate':
            l = l[l.find('generate')+8:]
        elif l[:11] == 'add process':
            l = l[l.find('add process')+11:]
        else:
            continue
        l = l.strip()
        #Get final states and process ID
        finalStates,iproc = l.split('>')[1].split('@')
        finalStates = finalStates.split(',')[0]
        finalStates = finalStates.strip().split()
        iproc = eval(iproc)
        #Store the process ID with its final states:
        if not iproc in finalStatesDict:        
            finalStatesDict[iproc] = finalStates
        else:
            logger.error("Error reading processes. Process ID %i appears more than once." %iproc)
            return False
    
    #Get total cross-section,number of events
    xsecTotal = banner.get_cross()
    if xsecTotal <= 0.:
        logger.error("Total cross-section is zero?")
        return False
    
    #Get sqrts and cross-section for each process:
    info = banner['init'].split('\n')[0].split()
    sqrts = eval(info[2]) + eval(info[3])
    pdgInitial = list(banner.get_pdg_beam())
    processXsecs = {}
    for l in banner['init'].split('\n')[1:]:
        if not l.strip() or l.strip()[0] == '<':
            continue
        vals = [eval(x) for x in l.split()]
        xsec,xsecErr,_,procID = vals
        if not procID in finalStatesDict:
            logger.error("Process ID %i found in LHE file" %procID)
            return False
        if not procID in processXsecs:
            processXsecs[procID] = {'xsec (pb)' : xsec, 'xsecErr (pb)' : xsecErr}
        else:
            logger.error("Error reading subprocess cross-sections. The process ID = %i appears multiple times" %procID)
            return False


    #Check:
    if abs(xsecTotal - sum([x['xsec (pb)'] for x in processXsecs.values()]))/xsecTotal > 0.001:
        logger.error("Total cross-section does not agree with sum of subprocesses")
        return False 
    
    #Write SLHA file:
    slhaF = open(slhaFile,'w')
    slhaF.write(slhaData)
    slhaF.write('\n\n')
    processXsecs = OrderedDict(sorted(processXsecs.items(), 
                                      key=lambda proc: proc[1]['xsec (pb)'],reverse=True))
    for procID in processXsecs:
        finalStates = finalStatesDict[procID]
        xsec = processXsecs[procID]['xsec (pb)']
        xsecErr = processXsecs[procID]['xsecErr (pb)']
        comment = "# xsec unit: pb xsec error: %1.3e" %(xsecErr)
        xsecLine = "\nXSECTION %1.3e " %(sqrts)
        xsecLine += " ".join([str(pdg) for pdg in pdgInitial])
        xsecLine += " %i " %len(finalStates)
        xsecLine += " ".join([str(pdg) for pdg in finalStates])
        slhaF.write(xsecLine+' '+comment+' \n')        
        slhaF.write("  0  0  0  0  0  0  %1.4e ufo2slha 1.0\n" %xsec)    
    slhaF.close()
    
    logger.info("Finished SLHA creation")
    
    return slhaFile


def runAll(parserDict):
    """
    Runs Madgraph, Pythia and the SLHA creator for a given set of options.
    :param parserDict: a dictionary with the parser options.
    """
    
    t0 = time.time() 
    
    parser = ConfigParserExt()
    parser.read_dict(parserDict)  
    
    #Run MadGraph
    if parser.getboolean('options','runMG'):
        Run_MG5(parser)

    #Create SLHA file
    if parser.getboolean("options","runSlhaCreator"):
        inputFile = parser.getvalue("slhaCreator","inputFile")
        if not os.path.isfile(inputFile):
            logger.error("Input file %s for SLHA creator not found" %inputFile)
        else:
            slhaFile = getSLHAFile(parser)
            if not slhaFile or not os.path.isfile(slhaFile):
                logger.error("Error creating SLHA file")
            else:
                logger.debug("File %s created" %slhaFile)
                
    #Clean output:
    if parser.getboolean("options","cleanOutFolders"):
        logger.info("Cleaning output")
        if os.path.isdir(parser.getvalue("MadGraphPars","mg5out")):
            shutil.rmtree(parser.getvalue("MadGraphPars","mg5out"))
          
    logger.info("Done in %3.2f min" %((time.time()-t0)/60.))
    now = datetime.datetime.now()
    
    return "Finished run at %s" %(now.strftime("%Y-%m-%d %H:%M"))


def main(parfile,verbose):
   
    level = verbose
    levels = { "debug": logging.DEBUG, "info": logging.INFO,
               "warn": logging.WARNING,
               "warning": logging.WARNING, "error": logging.ERROR }
    if not level in levels:
        logger.error ( "Unknown log level ``%s'' supplied!" % level )
        sys.exit()
    logger.setLevel(level = levels[level])    

    parser = ConfigParserExt( inline_comment_prefixes=( ';', ) )   
    ret = parser.read(parfile)
    if ret == []:
        logger.error( "No such file or directory: '%s'" % args.parfile)
        sys.exit()
            
    
    loopVars = []
    varValues = []
    for section in parser.sections():
        if section == 'options':
            continue
        for option in parser.options(section):
            v = parser.getvalue(section,option,raw=True)
            if not isinstance(v,list):
                v = [v]
            loopVars.append(option)
            varValues.append(v)

    ncpus = parser.getint("options","ncpu")
    if ncpus  < 0:
        ncpus =  multiprocessing.cpu_count()

    pool = multiprocessing.Pool(processes=ncpus)
    children = []
    #Loop over model parameters and submit jobs
    firstRun = True
    for values in itertools.product(*varValues):
        newParser = ConfigParserExt()
        newParser.read_dict(parser.toDict())
        for i,v in enumerate(values):        
            for section in newParser.sections():
                if loopVars[i] in newParser.options(section):        
                    newParser.set(section,loopVars[i],str(v))
        if firstRun and newParser.getboolean('options','runMG'):
            if not os.path.isdir(newParser.getvalue('MadGraphPars','processFolder')):
                generateProcesses(newParser)
                firstRun = False
        parserDict = newParser.toDict(raw=False) #Must convert to dictionary for pickling
        p = pool.apply_async(runAll, args=(parserDict,))            
        children.append(p)
        
#     Wait for jobs to finish:
    output = [p.get() for p in children]
    return output

    


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run MadGraph and Pythia in order to compute efficiencies for a given model." )
    ap.add_argument('-p', '--parfile', default='slha_parameters.ini',
            help='path to the parameters file. Parameters not defined in the parfile will be read from eff_parameters_default.ini')
    ap.add_argument('-v', '--loglevel', default='error',
            help='verbose level (debug, info, warning or error). Default is error')


    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile,args.verbose)
            
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
