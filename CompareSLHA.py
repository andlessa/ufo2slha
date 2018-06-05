
# coding: utf-8

# In[1]:


import pyslha,itertools
import logging as logger


# In[13]:


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
        return obj1 == obj2
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
                    logger.warning( 'The values are: %s versus %s'%                                ( s1,s2 ) )
                return False
    elif isinstance(obj1,list):
        if len(obj1) != len(obj2):
            logger.warning('Lists differ in length:\n   %i (this run)\n and\n   %i (default)' %                                (len(obj1),len(obj2)))
            return False
        for ival,val in enumerate(obj1):
            if not equalObjs(val,obj2[ival],rtol):
                logger.warning('Lists differ:\n   %s (this run)\n and\n   %s (default)' %                                (str(val),str(obj2[ival])))
                return False
    else:
        if not equalObjs(obj1.__dict__,obj2.__dict__):
            return False
        
    return True


# In[14]:


#Load the SLHA data
slhaFiles = {'andre' : './test_13.slha', 'juhi' : './param_card_1_f1TeV.dat'}
slhaData = dict([[key,pyslha.readSLHAFile(val)] for key,val in slhaFiles.items()])


# In[15]:


#Loop over the files and compare them 2 at a time:
for file1,file2 in itertools.product(slhaData.keys(),slhaData.keys()):
    if file1 == file2:
        continue
    slha1 = slhaData[file1]
    slha2 = slhaData[file2]
    comp = equalObjs(slha1,slha2)
    if not comp:
        print('Files %s and %s differ' %(file1,file2))


# In[11]:


print(len(slhaData['juhi'].xsections))
print(len(slhaData['andre'].xsections))

