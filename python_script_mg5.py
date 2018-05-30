import os
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2")
os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/editparam.py')
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2/")
os.system('./bin/mg5_aMC ./text.py') 
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2")
os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/cross_section2.py')
     
    
print  "Goodbye"

