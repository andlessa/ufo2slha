import os
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2")
os.system('./mg5_aMC ./text_createfolders.py') 
# edit param card  #default f    too many text files, easier way to input using function

for f in range(1000,1050,50):
    for k in range(1,2,1):
        A=open('f.txt','w+')
        A.write(str(f))
        B = open('k.txt','w+')
        B.write(str(k*0.5))
        #write a function which writes param_card with f, k as inputs 
      
        os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/editparam.py')
        os.system('./mg5_aMC ./MG5run.py') 
        #os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/")
        os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/cross_section3.py')
  #  os.system('rm -rf *sample1/Events/*')
print  "Goodbye"

