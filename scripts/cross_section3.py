#!/usr/bin/env python
import gzip
pids={'dh':8880001,'dh~':-8880001,'uh':8880002,'uh~':-8880002,'sh':8880003,'sh~':-8880003,'ch':8880004,'ch~':-8880004,
'bh':8880005,'bh~':-8880005,'th':8880006,'th~':-8880006,'thodd':8880007,'thodd~':-8880007,'eh-':8880011,'eh+':-8880011,
'veh':8880012,'veh~':-8880012,'muh-':8880013,'vmh':8880014,'muh+':-8880013,'vmh~':-8880014,'tah-':8880015,'vth':8880016,'tah+':-8880015,'vth~':-8880016,'ah':8880022,'zh':8880023,'wh+':8880024,'wh-':-8880024,'phi0':8880025,'phip':8880027,'phim':-8880027,'phips':8880026, 'theven':8880008,'theven~':-8880008}

process=['WHWH_sample1','ahah_sample1','zhzh_sample1',
'zhah_sample1','zhwhp_sample1','zhwhm_sample1',
'ahwhp_sample1','ahwhm_sample1','thotho_sample1',
'uhuh_sample1','dhdh_sample1','chch_sample1',
'shsh_sample1','uhbuhb_sample1','dhbdhb_sample1',
'chbchb_sample1','shbshb_sample1','uhdhb_sample1',
'uhbdh_sample1','uhshb_sample1','uhbsh_sample1',
'uhchb_sample1','uhbch_sample1','dhbch_sample1',
'dhchb_sample1','dhshb_sample1','dhbsh_sample1',
'uhdh_sample1','uhch_sample1','uhsh_sample1',
'dhch_sample1','dhsh_sample1','chsh_sample1',
'eheh_sample1','mupmum_sample1','tahptahm_sample1',
'vehvehb_sample1','vmhvmhb_sample1','vthvthb_sample1',
'bhbhb_sample1','bhbh_sample1','bhbbhb_sample1',
'phi0phi0_sample1','phi0phip_sample1','phi0phim_sample1',
'phipphim_sample1','phipsphi0_sample1','phipsphip_sample1',
'phipsphim_sample1','ththb_sample1','ehpveh_sample1',
'ehmveh_sample1','muhpvmh_sample1','muhmvmh_sample1',
'tahpvth_sample1','tahmvth_sample1','uhuhb_sample1',
'dhdhb_sample1','chchb_sample1','shshb_sample1',
'shchb_sample1','chshb_sample1','uhzh_sample1',
'uhah_sample1','uhbzh_sample1','uhbah_sample1',
'uhbwhp_sample1','uhwhm_sample1','dhzh_sample1',
'dhah_sample1','dhbzh_sample1','dhbah_sample1',
'dhbwhm_sample1','dhwhp_sample1','chzh_sample1',
'chah_sample1','chbzh_sample1','chbah_sample1',
'chbwhp_sample1','chwhm_sample1','shzh_sample1',
'shah_sample1','shbzh_sample1','shbah_sample1',
'shwhp_sample1','shbwhm_sample1','ahbh_sample1',
'ahbhb_sample1','thwhm_sample1','thbwhp_sample1',
'uhbchb_sample1','uhbshb_sample1','uhbdhb_sample1',
'uhbbhb_sample1','uhbth_sample1','dhbchb_sample1',
'dhbshb_sample1','dhbbhb_sample1','dhbthb_sample1',
'shbchb_sample1','shbbhb_sample1','shbthb_sample1',
'chbbhb_sample1','chbth_sample1','bhthb_sample1',
'bhbth_sample1','shbh_sample1','shbbh_sample1',
'shbbhb_sample1','phi0zh_sample1','phi0ah_sample1',
'phipzh_sample1','phipah_sample1','phipwhm_sample1',
'phimzh_sample1','phimah_sample1','phimwhp_sample1',
'phipszh_sample1','phipsah_sample1','phipswhp_sample1','phipswhm_sample1','thethe_sample1','phipsphips_sample1'] 
pid1=[pids['wh-'],pids['ah'],pids['zh'],
pids['ah'],pids['zh'],pids['wh-'],
pids['ah'],pids['wh-'],pids['thodd~'],
pids['uh'],pids['dh'],pids['ch'],
pids['sh'],pids['uh~'],pids['dh~'],
pids['ch~'],pids['sh~'],pids['dh~'],
pids['uh~'],pids['sh~'],pids['uh~'],
pids['ch~'],pids['uh~'],pids['dh~'],
pids['ch~'],pids['sh~'],pids['dh~'],
pids['dh'],pids['uh'],pids['uh'],
pids['dh'],pids['dh'],pids['sh'],
pids['eh+'],pids['muh+'],pids['tah+'],
pids['veh~'],pids['vmh~'],pids['vth~'],
pids['bh~'],pids['bh'],pids['bh~'],
pids['phi0'],pids['phi0'],pids['phim'],
pids['phim'],pids['phi0'],pids['phips'],
pids['phim'],pids['th~'],pids['eh+'],
pids['veh~'],pids['muh+'],pids['vmh~'],
pids['tah+'],pids['vth~'],pids['uh~'],
pids['dh~'],pids['ch~'],pids['sh~'],
pids['ch~'],pids['sh~'],pids['uh'],
pids['uh'],pids['uh~'],pids['uh~'],
pids['uh~'],pids['wh-'],pids['dh'],
pids['dh'],pids['dh~'],pids['dh~'],
pids['wh-'],pids['dh'],pids['ch'],
pids['ch'],pids['ch~'],pids['ch~'],
pids['ch~'],pids['wh-'],pids['sh'],
pids['sh'],pids['sh~'],pids['sh~'],
pids['sh'],pids['wh-'],pids['ah'],
pids['bh~'],pids['wh-'],pids['th~'],
pids['ch~'],pids['sh~'],pids['uh~'],
pids['bh~'],pids['uh~'],pids['ch~'],
pids['sh~'],pids['bh~'],pids['th~'],
pids['ch~'],pids['bh~'],pids['th~'],
pids['bh~'],pids['ch~'],pids['th~'],
pids['bh~'],pids['sh'],pids['bh~'],pids['sh~'],
pids['zh'],pids['ah'],pids['zh'],
pids['ah'],pids['wh-'],pids['phim'],
pids['phim'],pids['phim'],pids['zh'],
pids['ah'],pids['wh+'],pids['wh-'],pids['theven~'],pids['phips']
]

pid2=[pids['wh+'],pids['ah'],pids['zh'],
pids['zh'],pids['wh+'],pids['zh'],
pids['wh+'],pids['ah'],pids['thodd'],
pids['uh'],pids['dh'],pids['ch'],
pids['sh'],pids['uh~'],pids['dh~'],
pids['ch~'],pids['sh~'],pids['uh'],
pids['dh'],pids['uh'],pids['sh'],
pids['uh'],pids['ch'],pids['ch'],
pids['dh'],pids['dh'],pids['sh'],
pids['uh'],pids['ch'],pids['sh'],
pids['ch'],pids['sh'],pids['ch'],
pids['eh-'],pids['muh-'],pids['tah-'],
pids['veh'],pids['vmh'],pids['vth'],
pids['bh'],pids['bh'],pids['bh~'],
pids['phi0'],pids['phip'],pids['phi0'],
pids['phip'],pids['phips'],pids['phip'],
pids['phips'],pids['th'],pids['veh'],
pids['eh-'],pids['vmh'],pids['muh-'],
pids['vth'],pids['tah-'],pids['uh'],
pids['dh'],pids['ch'],pids['sh'],
pids['sh'],pids['ch'],pids['zh'],
pids['ah'],pids['zh'],pids['ah'],
pids['wh+'],pids['uh'],pids['zh'],
pids['ah'],pids['zh'],pids['ah'],
pids['dh~'],pids['wh+'],pids['zh'],
pids['ah'],pids['zh'],pids['ah'],
pids['wh+'],pids['ch'],pids['zh'],
pids['ah'],pids['zh'],pids['ah'],
pids['wh+'],pids['sh~'],pids['bh'],
pids['ah'],pids['th'],pids['wh+'],
pids['uh~'],pids['uh~'],pids['dh~'],
pids['uh~'],pids['th'],pids['dh~'],
pids['dh~'],pids['dh~'],pids['dh~'],
pids['sh~'],pids['sh~'],pids['sh~'],
pids['ch~'],pids['th'],pids['bh'],
pids['th'],pids['bh'],pids['sh~'],pids['sh~'],
pids['phi0'],pids['phi0'],pids['phip'],
pids['phip'],pids['phip'],pids['zh'],
pids['ah'],pids['wh+'],
pids['phips'],pids['phips'],pids['phips'],pids['phips'],pids['theven'],pids['phips']]

print len(process)
print len(pids)
print len(pid1)
print len(pid2)

a=0
file2=open('/home/recapp/Downloads/MG5_aMC_v2_6_2/thotho_sample1/Cards/param_card.dat','a')
#print len(process)
nevents=0
cross_section=0
zerocs=0
file3=open('/home/recapp/Downloads/MG5_aMC_v2_6_2/NewCS8.dat','a')
for a in range (0,len(process),1):
    #file=gzip.open('/home/recapp/Downloads/MG5_aMC_v2_6_2/'+str(process[a])+'/Events/run_01/unweighted_events.lhe.gz','r')
    file=open('/home/recapp/Downloads/MG5_aMC_v2_6_2/'+str(process[a])+'/Events/run_01/run_01_tag_1_banner.txt','r')
    #if not os.path.isfile(file):file.split("\n"), 
          # continue   
    #if a==40 or a==41:
     #                 print process[a]
    for line in file:
        if "#  Number of Events        :" in line:
           nevents=((line.split(":")[1]).lstrip()).rstrip()
      
        if "#  Integrated weight (pb)  :   " in line:
            cross_section=((line.split(":")[1]).lstrip()).rstrip()
          #  print a
        
            file2.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pid1[a])+" "+str(pid2[a])+" # "+str(nevents)+" events, [pb],   MG5 for LO "+"\n")
            file2.write("     0 0 0 0 0 0 "+str(cross_section) +" # for Littlest Higgs Model with T Parity"+"\n")
            file3.write(str(cross_section)+" "+str(a)+" "+process[a]+ " "+str(pid1[a])+" "+str(pid2[a])+"\n")
        
        else: 
            continue
      
