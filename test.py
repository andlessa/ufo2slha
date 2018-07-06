#!/usr/bin/env python

#A wrapper for ConfigParser which allows to evaluate expressions
#in the parameters. The expressions should be of the type ${expr}.
#References for other parameters in the parser should be in the format section:parameter.

from ConfigParser import SafeConfigParser,InterpolationDepthError,MAX_INTERPOLATION_DEPTH
from math import *
import glob
import re




class ConfigParserExt(SafeConfigParser):
    
    
    def __init__(self,*args,**kargs):
        SafeConfigParser.__init__(self,*args,**kargs)
        self.cur_depth = 0 

    def toDict(self,raw=True):
        """
        Convert parser to dictionary.
        If raw=True, will return the raw values, otherwise it will
        try to evaluate them.
        """
        
        parserDict = {}
        for s in self.sections():
            parserDict[s] = {}
            for var in self.options(s):
                parserDict[s][var] = self.getvalue(s,var,raw=raw)
        
        return parserDict
    
    def get(self, section, option, raw=False, vars=None):
        r_opt = SafeConfigParser.get(self, section, option, raw=True, vars=vars)
        if raw:
            return r_opt

        ret = r_opt
        re_oldintp = r'%\((\w*)\)s'
        re_newintp = r'\$\{(\w*):(\w*)\}'

        m_new = re.findall(re_newintp, r_opt)
        if m_new:
            for f_section, f_option in m_new:
                self.cur_depth = self.cur_depth + 1 
                if self.cur_depth < MAX_INTERPOLATION_DEPTH:
                    sub = self.get(f_section, f_option, vars=vars)
                    ret = ret.replace('${{{0}:{1}}}'.format(f_section, f_option), sub)
                else:
                    raise InterpolationDepthError, (option, section, r_opt)

        m_old = re.findall(re_oldintp, r_opt)
        if m_old:
            for l_option in m_old:
                self.cur_depth = self.cur_depth + 1 
                if self.cur_depth < MAX_INTERPOLATION_DEPTH:
                    sub = self.get(section, l_option, vars=vars)
                    print('ret=',ret,sub)
                    ret = ret.replace('%({0})s'.format(l_option), sub)
                else:
                    raise InterpolationDepthError, (option, section, r_opt)
            
    def Get(self,*args,**kargs):
        """
        Return value with expressions evaluated
        """
        
        #First try to call get directly
        try:
            val = self.get(*args,**kargs)
            return val
        #If fails, get the raw expression and try to evaluate it.
        except:
            if not kargs:
                kargs = {}
            kargs['raw'] = True
            #Get raw expression:
            val = self.get(*args,**kargs)            
            return val
        
    def getstr(self,*args,**kargs):
        
        return str(self.get(*args,**kargs))
        

    def getvalue(self,*args,**kargs):
        
        val = self.get(*args,**kargs)
        try:
            val = eval(val)
        except:
            pass
        
        return val



if __name__ == "__main__":
    
    parFile = 'test.ini'
    
    parser = ConfigParserExt()
    ret = parser.read(parFile)
#     ret = parser.read('slha-parameters.ini')
    
#     print(parser.get("MadGraphPars","mg5out"))
#     print(parser.sections())
#     print(parser.toDict(raw=True))
    print(parser.get('MadGraphSet','MHt'))
    print(parser.Get('MadGraphSet','MHt'))
    print(parser.get('MadGraphSet','MHe'))
    print(parser.get('MadGraphSet','MHve'))
    
    
    
            
