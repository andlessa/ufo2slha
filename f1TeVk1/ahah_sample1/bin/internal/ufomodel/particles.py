# This file was automatically created by FeynRules 2.3.27
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Fri 4 Aug 2017 17:45:20


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     LeptonNumber = 0,
                     Y = 0,
                     Y1 = 0,
                     Y2 = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

AH = Particle(pdg_code = 8880022,
              name = 'AH',
              antiname = 'AH',
              spin = 3,
              color = 1,
              mass = Param.MAH,
              width = Param.ZERO,
              texname = 'AH',
              antitexname = 'AH',
              charge = 0,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

ZH = Particle(pdg_code = 8880023,
              name = 'ZH',
              antiname = 'ZH',
              spin = 3,
              color = 1,
              mass = Param.MZH,
              width = Param.WZH,
              texname = 'ZH',
              antitexname = 'ZH',
              charge = 0,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

WH__plus__ = Particle(pdg_code = 8880024,
                      name = 'WH+',
                      antiname = 'WH-',
                      spin = 3,
                      color = 1,
                      mass = Param.MWH,
                      width = Param.WWH,
                      texname = 'WH+',
                      antitexname = 'WH-',
                      charge = 1,
                      LeptonNumber = 0,
                      Y = 0,
                      Y1 = 0,
                      Y2 = 0)

WH__minus__ = WH__plus__.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              LeptonNumber = 1,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              LeptonNumber = 1,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              LeptonNumber = 1,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      LeptonNumber = 1,
                      Y = 0,
                      Y1 = 0,
                      Y2 = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MM,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       LeptonNumber = 1,
                       Y = 0,
                       Y1 = 0,
                       Y2 = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       LeptonNumber = 1,
                       Y = 0,
                       Y1 = 0,
                       Y2 = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

b__tilde__ = b.anti()

veH = Particle(pdg_code = 8880012,
               name = 'veH',
               antiname = 'veH~',
               spin = 2,
               color = 1,
               mass = Param.MHve,
               width = Param.WHve,
               texname = 'veH',
               antitexname = 'veH~',
               charge = 0,
               LeptonNumber = 1,
               Y = 0,
               Y1 = 0,
               Y2 = 0)

veH__tilde__ = veH.anti()

vmH = Particle(pdg_code = 8880014,
               name = 'vmH',
               antiname = 'vmH~',
               spin = 2,
               color = 1,
               mass = Param.MHvm,
               width = Param.WHvm,
               texname = 'vmH',
               antitexname = 'vmH~',
               charge = 0,
               LeptonNumber = 1,
               Y = 0,
               Y1 = 0,
               Y2 = 0)

vmH__tilde__ = vmH.anti()

vtH = Particle(pdg_code = 8880016,
               name = 'vtH',
               antiname = 'vtH~',
               spin = 2,
               color = 1,
               mass = Param.MHvt,
               width = Param.WHvt,
               texname = 'vtH',
               antitexname = 'vtH~',
               charge = 0,
               LeptonNumber = 1,
               Y = 0,
               Y1 = 0,
               Y2 = 0)

vtH__tilde__ = vtH.anti()

eH__minus__ = Particle(pdg_code = 8880011,
                       name = 'eH-',
                       antiname = 'eH+',
                       spin = 2,
                       color = 1,
                       mass = Param.MHe,
                       width = Param.WHe,
                       texname = 'eH-',
                       antitexname = 'eH+',
                       charge = -1,
                       LeptonNumber = 1,
                       Y = 0,
                       Y1 = 0,
                       Y2 = 0)

eH__plus__ = eH__minus__.anti()

muH__minus__ = Particle(pdg_code = 8880013,
                        name = 'muH-',
                        antiname = 'muH+',
                        spin = 2,
                        color = 1,
                        mass = Param.MHmu,
                        width = Param.WHmu,
                        texname = 'muH-',
                        antitexname = 'muH+',
                        charge = -1,
                        LeptonNumber = 1,
                        Y = 0,
                        Y1 = 0,
                        Y2 = 0)

muH__plus__ = muH__minus__.anti()

taH__minus__ = Particle(pdg_code = 8880015,
                        name = 'taH-',
                        antiname = 'taH+',
                        spin = 2,
                        color = 1,
                        mass = Param.MHta,
                        width = Param.WHta,
                        texname = 'taH-',
                        antitexname = 'taH+',
                        charge = -1,
                        LeptonNumber = 1,
                        Y = 0,
                        Y1 = 0,
                        Y2 = 0)

taH__plus__ = taH__minus__.anti()

uH = Particle(pdg_code = 8880002,
              name = 'uH',
              antiname = 'uH~',
              spin = 2,
              color = 3,
              mass = Param.MHu,
              width = Param.WHu,
              texname = 'uH',
              antitexname = 'uH~',
              charge = 2/3,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

uH__tilde__ = uH.anti()

cH = Particle(pdg_code = 8880004,
              name = 'cH',
              antiname = 'cH~',
              spin = 2,
              color = 3,
              mass = Param.MHc,
              width = Param.WHc,
              texname = 'cH',
              antitexname = 'cH~',
              charge = 2/3,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

cH__tilde__ = cH.anti()

tH = Particle(pdg_code = 8880006,
              name = 'tH',
              antiname = 'tH~',
              spin = 2,
              color = 3,
              mass = Param.MHt,
              width = Param.WHt,
              texname = 'tH',
              antitexname = 'tH~',
              charge = 2/3,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

tH__tilde__ = tH.anti()

dH = Particle(pdg_code = 8880001,
              name = 'dH',
              antiname = 'dH~',
              spin = 2,
              color = 3,
              mass = Param.MHd,
              width = Param.WHd,
              texname = 'dH',
              antitexname = 'dH~',
              charge = -1/3,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

dH__tilde__ = dH.anti()

sH = Particle(pdg_code = 8880003,
              name = 'sH',
              antiname = 'sH~',
              spin = 2,
              color = 3,
              mass = Param.MHs,
              width = Param.WHs,
              texname = 'sH',
              antitexname = 'sH~',
              charge = -1/3,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

sH__tilde__ = sH.anti()

bH = Particle(pdg_code = 8880005,
              name = 'bH',
              antiname = 'bH~',
              spin = 2,
              color = 3,
              mass = Param.MHb,
              width = Param.WHb,
              texname = 'bH',
              antitexname = 'bH~',
              charge = -1/3,
              LeptonNumber = 0,
              Y = 0,
              Y1 = 0,
              Y2 = 0)

bH__tilde__ = bH.anti()

THodd = Particle(pdg_code = 8880007,
                 name = 'THodd',
                 antiname = 'THodd~',
                 spin = 2,
                 color = 3,
                 mass = Param.MHTodd,
                 width = Param.WHTodd,
                 texname = 'THodd',
                 antitexname = 'THodd~',
                 charge = 2/3,
                 LeptonNumber = 0,
                 Y = 0,
                 Y1 = 0,
                 Y2 = 0)

THodd__tilde__ = THodd.anti()

THeven = Particle(pdg_code = 8880008,
                  name = 'THeven',
                  antiname = 'THeven~',
                  spin = 2,
                  color = 3,
                  mass = Param.MHTeven,
                  width = Param.WHTeven,
                  texname = 'THeven',
                  antitexname = 'THeven~',
                  charge = 2/3,
                  LeptonNumber = 0,
                  Y = 0,
                  Y1 = 0,
                  Y2 = 0)

THeven__tilde__ = THeven.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             LeptonNumber = 0,
             Y = 0,
             Y1 = 0,
             Y2 = 0)

phi0 = Particle(pdg_code = 8880025,
                name = 'phi0',
                antiname = 'phi0',
                spin = 1,
                color = 1,
                mass = Param.MPhi0,
                width = Param.WPhi0,
                texname = 'phi0',
                antitexname = 'phi0',
                charge = 0,
                LeptonNumber = 0,
                Y = 0,
                Y1 = 0,
                Y2 = 0)

phiP = Particle(pdg_code = 8880026,
                name = 'phiP',
                antiname = 'phiP',
                spin = 1,
                color = 1,
                mass = Param.MPhiP,
                width = Param.WPhiP,
                texname = 'phiP',
                antitexname = 'phiP',
                charge = 0,
                LeptonNumber = 0,
                Y = 0,
                Y1 = 0,
                Y2 = 0)

phi__plus__ = Particle(pdg_code = 8880027,
                       name = 'phi+',
                       antiname = 'phi-',
                       spin = 1,
                       color = 1,
                       mass = Param.MPhiC,
                       width = Param.WPhiC,
                       texname = 'phi+',
                       antitexname = 'phi-',
                       charge = 1,
                       LeptonNumber = 0,
                       Y = 0,
                       Y1 = 0,
                       Y2 = 0)

phi__minus__ = phi__plus__.anti()

phi__plus____plus__ = Particle(pdg_code = 8880028,
                               name = 'phi++',
                               antiname = 'phi--',
                               spin = 1,
                               color = 1,
                               mass = Param.MPhiCC,
                               width = Param.WPhiCC,
                               texname = 'phi++',
                               antitexname = 'phi--',
                               charge = 2,
                               LeptonNumber = 0,
                               Y = 0,
                               Y1 = 0,
                               Y2 = 0)

phi__minus____minus__ = phi__plus____plus__.anti()

