#!/usr/bin/env python

"""
.. module:: particles
   :synopsis: Defines the list of R-even and R-odd particles to be used.

.. moduleauthor:: Andre Lessa <lessa.a.p@gmail.com>

   :parameter rOdd: dictionary with PDG codes for the rOdd (Z2-odd) particles
   and their respective labels
   :parameter rEven: dictionary with PDG codes for the rEven (Z2-eveb)
   particles and their respective labels
   :parameter ptcDic: dictionary with inclusive labels to help defining group
   of particles in the analysis database
   
   HOW TO ADD NEW PARTICLES: simply add a new entry in rOdd (rEven) if the
   particle is Z2-odd (Z2-even). For now all decays of Z2-even particles are
   ignored. Z2-odd particles are decayed assuming Z2 conservation.
   
   If you want to use slhaChecks to verify your input file (in the case of SLHA input
   only), also include the quantum numbers of the new particles in the qNumbers dictionary below.

"""


rOdd = {8880001 : "dH",
        8880002 : "uH",
        8880003 : "sH",
        8880004 : "cH",
        8880005 : "bH",
        8880006 : "tH",
        8880007 : "THodd",
        8880008 : "THeven",
        8880011 : "eH",
        8880012 : "veH",
        8880013 : "muH",
        8880014 : "vmH",
        8880015 : "tauH",
        8880016 : "vtH",
        8880022 : "AH",
        8880023 : "ZH",
        8880024 : "WH",
        8880025 : "Phi0",
        8880026 : "PhiP",
        8880027 : "Phi+",
        8880028 : "Phi++",
       -8880001 : "dH",
       -8880002 : "uH",
       -8880003 : "sH",
       -8880004 : "cH",
       -8880005 : "bH",
       -8880006 : "tH",
       -8880007 : "THodd",
       -8880008 : "THeven",
       -8880011 : "eH",
       -8880012 : "veH",
       -8880013 : "muH",
       -8880014 : "vmH",
       -8880015 : "tauH",
       -8880016 : "vtH",
       -8880022 : "AH",
       -8880023 : "ZH",
       -8880024 : "WH",
       -8880025 : "Phi0",
       -8880026 : "PhiP",
       -8880027 : "Phi+",
       -8880028 : "Phi++"
 }

rEven = {25 : "higgs",
        -25 : "higgs",
         35 : "H0",
        -35 : "H0",
         36 : "A0",
        -36 : "A0",
         37 : "H+",
        -37 : "H-",
         23 : "Z",
        -23 : "Z",
         22 : "photon",
        -22 : "photon",
         24 : "W+",
        -24 : "W-",
         16 : "nu",
        -16 : "nu",
         15 : "ta-",
        -15 : "ta+",
         14 : "nu",
        -14 : "nu",
         13 : "mu-",
        -13 : "mu+",
         12 : "nu",
        -12 : "nu",
         11 : "e-",
        -11 : "e+",
         4  : "c",
        -4  : "c",
         5  : "b",
        -5  : "b",
         6  : "t+",
        -6  : "t-",
         1  : "q",
         2  : "q",
         3  : "q",
         -1  : "q",
         -2  : "q",
         -3  : "q",
         21  : "g",
         -21  : "g",
         111: "pi",
         -111: "pi",
         211: "pi",
         -211: "pi"
}

#Particle dictionary. Convenient for defining multiple particles with one label.
ptcDic = {"e"  : ["e+",  "e-"],
          "mu" : ["mu+", "mu-"],
          "ta" : ["ta+", "ta-"],
          "l+" : ["e+",  "mu+"],
          "l-" : ["e-",  "mu-"],
          "l"  : ["e-",  "mu-", "e+", "mu+"],
          "W"  : ["W+",  "W-"],
          "t"  : ["t+",  "t-"],
          "L+" : ["e+",  "mu+", "ta+"],
          "L-" : ["e-",  "mu-", "ta-"],
          "L"  : ["e+",  "mu+", "ta+", "e-", "mu-", "ta-"],
          "jet" : [ "q", "g", "c", "pi" ],
          "all" : ["e+",  "mu+", "ta+", "e-", "mu-", "ta-", "W+", "W-","Z","photon","higgs","t+","t-","b","c","q","g","c","pi"]}

#Quantum numbers for the new particles. Just used by tools.slhaChecks
#PDG: (spin*2, electrical charge*3, color dimension)
qNumbers={
 35:[0,0,1],
 36:[0,0,1],
 37:[0,3,1],
 8880001:[1,-1,3],
 8880002:[1,2,3],
 8880003:[1,-1,3],
 8880004:[1,2,3],
 8880005:[1,-1,3],
 8880006:[1,2,3],
 8880007:[1,-2,3],
 8880008:[1,2,3],
 8880011:[1,3,1],
 8880012:[1,0,1],
 8880013:[1,3,1],
 8880014:[1,0,1],
 8880015:[1,3,1],
 8880016:[1,0,1],
 8880022:[2,0,1],
 8880023:[2,0,1],
 8880024:[2,3,1],
 8880025:[0,0,1],
 8880026:[0,0,1],
 8880027:[0,3,1],
 8880028:[0,6,1],
 1000111:[1,3,1],
 1000255:[0,0,1] 
}

