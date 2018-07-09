#!/usr/bin/env python

"""
.. module:: testCreator
   :synopsis: Tests the slha creator

.. moduleauthor:: Andre Lessa <lessa.a.p@gmail.com>

"""
import sys,os,shutil,glob
sys.path.insert(0,"../")
import unittest
from configParserWrapperNEW import ConfigParserExt
from createSLHA import main

class CreatorTest(unittest.TestCase):
    
    
    def testConfigParserWrapper(self):

        parFile = 'test.ini'    
        parser = ConfigParserExt()
        parser.read(parFile)
        rawDict = {'MadGraphPars': {'processFolder': 'outputDir/MG5_output/proc-littleHiggs', 
                                    'ncores': 1, 'runcard': 'inputCards/run_card.dat', 
                                    'paramcard': 'inputCards/param_card-littleHiggs.dat', 
                                    'mg5out': '"outputDir/MG5_output/MHd_%.1f_%iTeV" %(${MadGraphSet:MHd},int((${MadGraphSet:ebeam1}+${MadGraphSet:ebeam2})/1000.))', 'MG5path': 'MG5'}, 
                                    'slhaCreator': {'inputFile': "${MadGraphPars:mg5out}/Events/run_01/unweighted_events.lhe.gz", 'slhaout': '"MHd_%.1f_%iTeV.slha" %(${MadGraphSet:MHd},int((${MadGraphSet:ebeam1}+${MadGraphSet:ebeam2})/1000.))'}, 
                   'options': {'runSlhaCreator': True, 'runMG': True, 'computeXsecsFor': [8880001, 8880002], 
                               'ncpu': -1, 'cleanOutFolders': True, 'modelFolder': 'UFO_LittleHiggs', 
                               'computeWidths': 'all --body_decay=2'}, 
                   'MadGraphSet': {'MHd': 2000.0, 'ebeam2': '${ebeam1}', 'ebeam1': 4000,
                                   'MHu': '${MHd}/2.', 'MHdd': '${MHu}+50', 'MHe': '${options:computeXsecsFor}[0]',
                                   'Mhve': '${MadGraphSet:MHe}*sqrt(4.)'}}
        valDict = {'MadGraphPars': {'processFolder': 'outputDir/MG5_output/proc-littleHiggs', 
                                    'ncores': 1, 'runcard': 'inputCards/run_card.dat', 
                                    'paramcard': 'inputCards/param_card-littleHiggs.dat', 
                                    'mg5out': 'outputDir/MG5_output/MHd_2000.0_8TeV', 'MG5path': 'MG5'}, 
                   'slhaCreator': {'inputFile': 'outputDir/MG5_output/MHd_2000.0_8TeV/Events/run_01/unweighted_events.lhe.gz', 
                                   'slhaout': 'MHd_2000.0_8TeV.slha'}, 
                   'options': {'runSlhaCreator': True, 'runMG': True, 
                               'computeXsecsFor': [8880001, 8880002], 'ncpu': -1, 
                               'cleanOutFolders': True, 'modelFolder': 'UFO_LittleHiggs', 
                               'computeWidths': 'all --body_decay=2'}, 
                   'MadGraphSet': {'MHd': 2000.0, 'ebeam2': 4000, 'ebeam1': 4000,
                                   'MHu': 1000.0, 'MHdd': 1050.0, 'MHe': 8880001, 'Mhve': 17760002.0}}


#         newDict =parser.toDict(raw=False)
#         oldDict = valDict        
        newDict =parser.toDict(raw=True)
        oldDict = rawDict 

        for s in newDict:
            for opt in newDict[s]:
                if not newDict[s][opt] == oldDict[s][opt]:
                    print(s,opt)
                    print(newDict[s][opt], oldDict[s][opt])
                    break
        self.assertEqual(parser.toDict(raw=True),rawDict)
        self.assertEqual(parser.toDict(raw=False),valDict)   


    def testSLHACreator(self):

        parFile = 'lhiggs_parameters.ini'
        if os.path.isdir('outputDir'):
            shutil.rmtree('outputDir')
        for f in glob.glob('./lhiggs_test_slha_*'):
            shutil.rmtree(f)
            
        out = main(parFile,'debug')

#         self.assertEqual(parser.toDict(raw=True),rawDict)
#         self.assertEqual(parser.toDict(raw=False),valDict)   

            

if __name__ == "__main__":
    unittest.main()
