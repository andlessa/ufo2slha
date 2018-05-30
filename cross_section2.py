#!/usr/bin/env python
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/WHWH_sample1/Events/run_01/run_01_tag_1_banner.txt"
file = open(textfile)
pdg1=8880024
pdg2=-8880024
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/ahah_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880022
pdg2=8880022
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/zhzh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880023
pdg2=8880023
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/zhah_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880023
pdg2=8880022
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/zhwhp_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880023
pdg2=8880024
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/zhwhm_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880023
pdg2=-8880024
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/ahwhp_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880024
pdg2=8880022
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/ahwhm_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880024
pdg2=8880022
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/thethe_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880008
pdg2=-8880008
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/thotho_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880007
pdg2=-8880007
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhuh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880002
pdg2=8880002
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhdh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880001
pdg2=8880001
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/chch_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880004
pdg2=8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/shsh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880003
pdg2=8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhbuhb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880002
pdg2=-8880002
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhbdhb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880001
pdg2=-8880001
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/chbchb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880004
pdg2=-8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/shbshb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880003
pdg2=8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhdhb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880002
pdg2=-8880001
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhbdh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880002
pdg2=8880001
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhshb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880002
pdg2=-8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhbsh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880002
pdg2=8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhchb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880002
pdg2=-8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhbch_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880002
pdg2=8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhchb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880001
pdg2=-8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhchb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880001
pdg2=8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhshb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880001
pdg2=-8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhbsh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880001
pdg2=8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhdh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880002
pdg2=8880001
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhch_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880002
pdg2=8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/uhsh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880002
pdg2=8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhch_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880001
pdg2=8880004
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/dhsh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880001
pdg2=8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/chsh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880004
pdg2=8880003
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/eheh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880011
pdg2=-8880011
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/mupmum_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880013
pdg2=-8880013
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/tahptahm_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880015
pdg2=-8880015
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/vehvehb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880012
pdg2=-8880012
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/vmhvmhb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880014
pdg2=-8880014
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/vthvthb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880016
pdg2=-8880016
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/bhbh_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880005
pdg2=8880005
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/bhbhb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880005
pdg2=-8880005
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/bhbbhb_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880005
pdg2=-8880005
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phi0phi0_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880025
pdg2=8880025
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phi0phip_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880025
pdg2=8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phi0phim_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880025
pdg2=-8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phipphim_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880027
pdg2=-8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phipsphi0_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880026
pdg2=8880025
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phipsphip_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880026
pdg2=8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phipsphim_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880026
pdg2=-8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phippphimm_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880028
pdg2=-8880028
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phippphim_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880028
pdg2=8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phippphim_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880028
pdg2=-8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phimmphip_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=-8880028
pdg2=8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")
textfile="/home/recapp/Downloads/MG5_aMC_v2_6_2/phippphim_sample1/Events/run_01/run_01_tag_1_banner.txt"
file=open(textfile)
pdg1=8880028
pdg2=-8880027
for line in file:
  if "Integrated weight" in line:
     file1=open("/home/recapp/Downloads/MG5_aMC_v2_6_2/param_card_2.dat","a")
     file1.write("\n"+"XSECTION 1.3E+04 2212 2212 2 "+str(pdg1)+" "+str(pdg2)+" # 10000 events, [pb], MG5 for LO "+"\n")
     file1.write("0 0 0 0 0 0 "+str(((line.split(":")[-1]).lstrip()).rstrip())+ " # for Littlest Higgs Model with T Parity"+"\n")


