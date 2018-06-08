import os
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2")
os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/editparam.py')
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2/")
os.system('./bin/mg5_aMC ./text_createfolders.py') 
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2/")
os.system('./bin/mg5_aMC ./MG5run.py') 
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2")
os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/cross_section3.py')
     
    
print  "Goodbye"

