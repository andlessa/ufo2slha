#!/usr/bin/env python

"""
.. module:: testCreator
   :synopsis: Tests the slha creator

.. moduleauthor:: Andre Lessa <lessa.a.p@gmail.com>

"""
import sys,os,shutil
sys.path.insert(0,"../")
import unittest
from configParserWrapper import ConfigParserExt
from createSLHA import main
import logging as logger
import pyslha



def equalObjs(obj1,obj2,rtol=0.01,ignore=[]):
    
    if type(obj1) != type(obj2):
        logger.warning("Data types differ (%s,%s)" %(type(obj1),type(obj2)))
        return False
   
    if type(obj1) in [ float, int ]:
        obj1,obj2=float(obj1),float(obj2)
    
    if isinstance(obj1,list):
        obj1 = sorted(obj1)
        obj2 = sorted(obj2)
    
    if obj1 == obj2:
        return True

    if isinstance(obj1,float):
        if obj1 == obj2:
            return True
        diff = 2.*abs(obj1-obj2)/abs(obj1+obj2)
        return diff < rtol
    elif isinstance(obj1,str):
        return obj1.lower() == obj2.lower()
    elif isinstance(obj1,dict):
        for key in obj1:
            if key in ignore:
                continue
            if not key in obj2:
                logger.warning("Key %s missing" %str(key))
                return False
            if not equalObjs(obj1[key],obj2[key],rtol, ignore=ignore ):
                logger.warning( "Dictionaries differ in key %s" %str(key))
                s1,s2 = str(obj1[key]),str(obj2[key]) 
                if len(s1) + len(s2) > 200:
                    logger.warning ( "The values are too long to print." )
                else:
                    logger.warning( 'The values are: %s versus %s'%\
                                ( s1,s2 ) )
                return False
    elif isinstance(obj1,list):
        if len(obj1) != len(obj2):
            logger.warning('Lists differ in length:\n   %i (this run)\n and\n   %i (default)' %\
                                (len(obj1),len(obj2)))
            return False
        for ival,val in enumerate(obj1):
            if not equalObjs(val,obj2[ival],rtol):
                logger.warning('Lists differ:\n   %s (this run)\n and\n   %s (default)' %\
                                (str(val),str(obj2[ival])))
                return False
    else:
        if not equalObjs(obj1.__dict__,obj2.__dict__):
            return False
        
    return True

class CreatorTest(unittest.TestCase):
    
    
    def testConfigParserWrapper(self):

        parFile = 'test.ini'    
        parser = ConfigParserExt()
        parser.read(parFile)
        rawDict = {'MadGraphPars': {'processFolder': 'outputDir/MG5_output/proc-littleHiggs', 
                                    'ncores': '1', 'runcard': 'inputCards/run_card.dat', 
                                    'paramcard': 'inputCards/param_card-littleHiggs.dat', 
                                    'mg5out': '"outputDir/MG5_output/MHd_%.1f_%iTeV" %(${MadGraphSet:MHd},int((${MadGraphSet:ebeam1}+${MadGraphSet:ebeam2})/1000.))', 'MG5path': 'MG5'}, 
                                    'slhaCreator': {'inputFile': "${MadGraphPars:mg5out}/Events/run_01/unweighted_events.lhe.gz", 
                                                    'slhaout': '"MHd_%.1f_%iTeV.slha" %(${MadGraphSet:MHd},int((${MadGraphSet:ebeam1}+${MadGraphSet:ebeam2})/1000.))',
                                                    'outputFolder' : "'./'"}, 
                   'options': {'runSlhaCreator': 'True', 'runMG': 'True', 'computeXsecsFor': '[8880001, 8880002]', 
                               'ncpu': '-1', 'cleanOutFolders': 'True', 'modelFolder': 'UFO_LittleHiggs', 
                               'computeWidths': 'all --body_decay=2'}, 
                   'MadGraphSet': {'MHd': '2000.0', 'ebeam2': '${ebeam1}', 'ebeam1': '4000',
                                   'MHu': '${MHd}/2.', 'MHdd': '${MHu}+50', 'MHe': '${options:computeXsecsFor}[0]',
                                   'Mhve': '${MadGraphSet:MHe}*sqrt(4.)'}}
        valDict = {'MadGraphPars': {'processFolder': 'outputDir/MG5_output/proc-littleHiggs', 
                                    'ncores': 1, 'runcard': 'inputCards/run_card.dat', 
                                    'paramcard': 'inputCards/param_card-littleHiggs.dat', 
                                    'mg5out': 'outputDir/MG5_output/MHd_2000.0_8TeV', 'MG5path': 'MG5'}, 
                   'slhaCreator': {'inputFile': 'outputDir/MG5_output/MHd_2000.0_8TeV/Events/run_01/unweighted_events.lhe.gz', 
                                   'slhaout': 'MHd_2000.0_8TeV.slha', 'outputFolder' : './'}, 
                   'options': {'runSlhaCreator': True, 'runMG': True, 
                               'computeXsecsFor': [8880001, 8880002], 'ncpu': -1, 
                               'cleanOutFolders': True, 'modelFolder': 'UFO_LittleHiggs', 
                               'computeWidths': 'all --body_decay=2'}, 
                   'MadGraphSet': {'MHd': 2000.0, 'ebeam2': 4000, 'ebeam1': 4000,
                                   'MHu': 1000.0, 'MHdd': 1050.0, 'MHe': 8880001, 'Mhve': 17760002.0}}


        newDict = parser.toDict(raw=True)
        oldDict = rawDict 
#         newDict = parser.toDict(raw=False)
#         oldDict = valDict
 
        for s in newDict:
            for opt in newDict[s]:
                if newDict[s][opt] != oldDict[s][opt]:
                    print(s,opt)
                    print('\t',newDict[s][opt], oldDict[s][opt])
#                     break

        self.assertEqual(parser.toDict(raw=True),rawDict)
        self.assertEqual(parser.toDict(raw=False),valDict)   


    def testSLHACreator(self):
   
        parFile = 'test_lhiggs.ini'
        if os.path.isdir('outputDir'):
            shutil.rmtree('outputDir')
        if os.path.isdir('testOutput'):
            shutil.rmtree('testOutput')
               
        out = main(parFile,'debug')
          
        self.assertTrue(len(out) == 4)
          
        outFiles = ['testOutput/test_F1000_8TeV.slha','testOutput/test_F500_8TeV.slha',
                    'testOutput/test_F1000_13TeV.slha','testOutput/test_F500_13TeV.slha']
          
        for f in outFiles:
            self.assertTrue(os.path.isfile(f))
          
        for f in outFiles:
            old = os.path.basename(f).replace('.slha','_default.slha')
            if not os.path.isfile(old):
                continue
            new = pyslha.readSLHAFile(f)
            old = pyslha.readSLHAFile(old)
            self.assertTrue(equalObjs(new, old, rtol=0.05))

            

if __name__ == "__main__":
    unittest.main()
