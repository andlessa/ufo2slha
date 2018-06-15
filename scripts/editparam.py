#!/usr/bin/env python
import os, sys
import math
#replace in param card.dat
file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card.dat.tpl","r+")
file2=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/scripts_2/param_card.dat","w+")
#print file
oldMHd=0.0
oldMHu=0.0
oldMHs=0.0
oldMHc=0.0
oldMHb=0.0
oldMHt=0.0
oldTHodd=0.0
oldTHeven=0.0
oldlep=0.0
oldAH=0.0
oldZH=0.0
oldWH=0.0
oldphi0=0.0
oldphip=0.0
oldphic=0.0
oldphiCc=0.0
f=0.0
kl=1.0
kq=1.0
k=1.0
R=1.0
oldf=0.0
oldkq=0.0
oldkl=0.0
newlep=0.0
g=0.663663
v=246.0
gprime=0.355435
mtop=172.5
mhiggs=125.6
# get scan input of k, f and set mass parameters
f2=open('f.txt','r')
k2=open('k.txt','r')
f=float(f2.read())
print f
k=float(k2.read())
print k
#provide the input such that it just replaces the param card.dat 
oldAH=(gprime*f*(1-(5.0*(v*1.0/f)**2)/8.0))/math.sqrt(5.0)
oldWH = (g*f*(1-(1.0*(v*1.0/f)**2)/8.0))
oldZH = (g*f*(1-(1.0*(v*1.0/f)**2)/8.0))
oldMHu=math.sqrt(2.0)*k*f*(1-(1.0*(v*1.0/f)**2)/8.0)
oldMHd=math.sqrt(2.0)*k*f
oldMHl=math.sqrt(2.0)*k*f
oldTHodd=(mtop*f*math.sqrt(2.0))/(v*1.0)
oldTHeven=oldTHodd*math.sqrt(2.0)
oldphi0=(1.0*math.sqrt(2.0)*f*mhiggs)/(v +(v*v*v)/(12*f*f))  
oldphip=oldphi0
oldphic=oldphi0
oldphiCc=oldphi0
oldlep=oldMHd
params=["oldf","oldlep","oldkf","oldkl","oldMHu","oldMHd","oldMHu","oldMHc","oldMHs","oldMHt","oldMHb","oldTHodd","oldTHeven","oldAH",
"oldWH","oldZH","oldphi0","oldphip","oldphic","oldphiCc"]
#replacing numbers in the param card
with file1 as fin:
     with file2 as fout:
          for line in fin:
               if "oldf" in line:
                   strA="oldf"
                   file2.write(line.replace(strA,str(f),1))
               if "oldlep" in line:
                   strB="oldlep"
                   file2.write(line.replace(strB,str(oldlep),5))
               if "oldkf" in line:
                   strC="oldkf"
                   file2.write(line.replace(strC,str(k),1))
               if "oldkl" in line:
                   strD="oldkl"
                   file2.write(line.replace(strD,str(k),1))
               if "oldMHu" in line:
                   strE="oldMHu"
                   file2.write(line.replace(strE,str(oldMHu),1))
               if "oldMHd" in line:
                   strF="oldMHd"
                   file2.write(line.replace(strF,str(oldMHd),1))
               if "oldMHc" in line:
                   strG="oldMHc"
                   file2.write(line.replace(strG,str(oldMHu),1))
               if "oldMHs" in line:
                   strH="oldMHs"
                   file2.write(line.replace(strH,str(oldMHd),1))
               if "oldMHt" in line:
                   strI="oldMHt"
                   file2.write(line.replace(strI,str(oldMHu),1))
               if "oldMHb" in line:
                   strJ="oldMHb"
                   file2.write(line.replace(strJ,str(oldMHd),1))
               if "oldTHodd" in line:
                   strK="oldTHodd"
                   file2.write(line.replace(strK,str(oldTHodd),1))
               if "oldTHeven" in line:
                   strL="oldTHeven"
                   file2.write(line.replace(strL,str(oldTHeven),1))
               if "oldAH" in line:
                   strM="oldAH"
                   file2.write(line.replace(strM,str(oldAH),1))
               if "oldWH" in line:
                   strN="oldWH"
                   file2.write(line.replace(strN,str(oldWH),1))
               if "oldZH" in line:
                   strO="oldZH"
                   file2.write(line.replace(strO,str(oldZH),1))
               if "oldphi0" in line:
                   strP="oldphi0"
                   file2.write(line.replace(strP,str(oldphi0),1))
               if "oldphip" in line:
                   strQ="oldphip"
                   file2.write(line.replace(strQ,str(oldphi0),1))
               if "oldphic" in line:
                   strR="oldphic"
                   file2.write(line.replace(strR,str(oldphi0),1))
               if "oldphiCc" in line:
                   strI="oldphiCc"
                   file2.write(line.replace(strI,str(oldphi0),1))
               else:
                   x=0
                   for params1 in params:                  
                      if params1 in line:
                             x=x+1
                             #print params1
                   if x==0:
                      file2.write(line)   

                         
