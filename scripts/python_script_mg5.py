import os, glob,shutil
os.chdir("/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2")
os.system('./mg5_aMC ./text_createfolders.py') 
# edit param card  #default f    too many text files, easier way to input using function
#os.system('./mg5_aMC ./MG5run.py')
#os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/cross_section3.py')


for f in range(550,600,50):
      for k in range(1,3,1):
        A=open('f.txt','w+')
        A.write(str(f))
        B = open('k.txt','w+')
        B.write(str(k*0.5))
        #write a function which writes param_card with f, k as inputs 
#        if not os.path.getsize("./f.txt")==0:
        os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/editparam.py')
        source="/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/param_card.dat"
        destination="/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/param_card/LHT%s%s.dat"%(f,k)
        shutil.copy(source,destination)
#      
        for path in glob.glob("/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/*sample1/Events/run_01/"):
               shutil.rmtree(path)
   
        if not os.path.getsize("./param_card.dat")==0:
           os.system('./mg5_aMC ./MG5run.py') 
  
           os.system('/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/cross_section3.py')
           source="/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/thethe_sample1/Cards/param_card.dat"
           destination="/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/slha/LHT%s%s.slha"%(f,k)
           shutil.move(source,destination)
          # for path in glob.glob("/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/*sample1/Events/run_01/"):
          #     shutil.rmtree(path)
print  "Goodbye"

  
