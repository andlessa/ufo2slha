# This file was automatically created by FeynRules 2.3.27
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Fri 4 Aug 2017 17:45:20



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

F = Parameter(name = 'F',
              nature = 'external',
              type = 'real',
              value = 1000,
              texname = 'F',
              lhablock = 'LHTBLOCK',
              lhacode = [ 1 ])

R = Parameter(name = 'R',
              nature = 'external',
              type = 'real',
              value = 1,
              texname = 'R',
              lhablock = 'LHTBLOCK',
              lhacode = [ 2 ])

k = Parameter(name = 'k',
              nature = 'external',
              type = 'real',
              value = 1,
              texname = 'k',
              lhablock = 'LHTBLOCK',
              lhacode = [ 3 ])

kl = Parameter(name = 'kl',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{kl}',
               lhablock = 'LHTBLOCK',
               lhacode = [ 4 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

sw2 = Parameter(name = 'sw2',
                nature = 'external',
                type = 'real',
                value = 0.23116,
                texname = '\\text{sw2}',
                lhablock = 'SMINPUTS',
                lhacode = [ 3 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 4 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 7 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 8 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 9 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.385,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

MAH = Parameter(name = 'MAH',
                nature = 'external',
                type = 'real',
                value = 150,
                texname = '\\text{MAH}',
                lhablock = 'MASS',
                lhacode = [ 8880022 ])

MZH = Parameter(name = 'MZH',
                nature = 'external',
                type = 'real',
                value = 400,
                texname = '\\text{MZH}',
                lhablock = 'MASS',
                lhacode = [ 8880023 ])

MWH = Parameter(name = 'MWH',
                nature = 'external',
                type = 'real',
                value = 400,
                texname = '\\text{MWH}',
                lhablock = 'MASS',
                lhacode = [ 8880024 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MHve = Parameter(name = 'MHve',
                 nature = 'external',
                 type = 'real',
                 value = 3000,
                 texname = '\\text{MHve}',
                 lhablock = 'MASS',
                 lhacode = [ 8880012 ])

MHvm = Parameter(name = 'MHvm',
                 nature = 'external',
                 type = 'real',
                 value = 3000,
                 texname = '\\text{MHvm}',
                 lhablock = 'MASS',
                 lhacode = [ 8880014 ])

MHvt = Parameter(name = 'MHvt',
                 nature = 'external',
                 type = 'real',
                 value = 3000,
                 texname = '\\text{MHvt}',
                 lhablock = 'MASS',
                 lhacode = [ 8880016 ])

MHe = Parameter(name = 'MHe',
                nature = 'external',
                type = 'real',
                value = 3000,
                texname = '\\text{MHe}',
                lhablock = 'MASS',
                lhacode = [ 8880011 ])

MHmu = Parameter(name = 'MHmu',
                 nature = 'external',
                 type = 'real',
                 value = 3000,
                 texname = '\\text{MHmu}',
                 lhablock = 'MASS',
                 lhacode = [ 8880013 ])

MHta = Parameter(name = 'MHta',
                 nature = 'external',
                 type = 'real',
                 value = 3000,
                 texname = '\\text{MHta}',
                 lhablock = 'MASS',
                 lhacode = [ 8880015 ])

MHu = Parameter(name = 'MHu',
                nature = 'external',
                type = 'real',
                value = 2800,
                texname = '\\text{MHu}',
                lhablock = 'MASS',
                lhacode = [ 8880002 ])

MHc = Parameter(name = 'MHc',
                nature = 'external',
                type = 'real',
                value = 2800,
                texname = '\\text{MHc}',
                lhablock = 'MASS',
                lhacode = [ 8880004 ])

MHt = Parameter(name = 'MHt',
                nature = 'external',
                type = 'real',
                value = 2800,
                texname = '\\text{MHt}',
                lhablock = 'MASS',
                lhacode = [ 8880006 ])

MHd = Parameter(name = 'MHd',
                nature = 'external',
                type = 'real',
                value = 3000,
                texname = '\\text{MHd}',
                lhablock = 'MASS',
                lhacode = [ 8880001 ])

MHs = Parameter(name = 'MHs',
                nature = 'external',
                type = 'real',
                value = 3000,
                texname = '\\text{MHs}',
                lhablock = 'MASS',
                lhacode = [ 8880003 ])

MHb = Parameter(name = 'MHb',
                nature = 'external',
                type = 'real',
                value = 3000,
                texname = '\\text{MHb}',
                lhablock = 'MASS',
                lhacode = [ 8880005 ])

MHTodd = Parameter(name = 'MHTodd',
                   nature = 'external',
                   type = 'real',
                   value = 600,
                   texname = '\\text{MHTodd}',
                   lhablock = 'MASS',
                   lhacode = [ 8880007 ])

MHTeven = Parameter(name = 'MHTeven',
                    nature = 'external',
                    type = 'real',
                    value = 650,
                    texname = '\\text{MHTeven}',
                    lhablock = 'MASS',
                    lhacode = [ 8880008 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MPhi0 = Parameter(name = 'MPhi0',
                  nature = 'external',
                  type = 'real',
                  value = 450,
                  texname = '\\text{MPhi0}',
                  lhablock = 'MASS',
                  lhacode = [ 8880025 ])

MPhiP = Parameter(name = 'MPhiP',
                  nature = 'external',
                  type = 'real',
                  value = 450,
                  texname = '\\text{MPhiP}',
                  lhablock = 'MASS',
                  lhacode = [ 8880026 ])

MPhiC = Parameter(name = 'MPhiC',
                  nature = 'external',
                  type = 'real',
                  value = 450,
                  texname = '\\text{MPhiC}',
                  lhablock = 'MASS',
                  lhacode = [ 8880027 ])

MPhiCC = Parameter(name = 'MPhiCC',
                   nature = 'external',
                   type = 'real',
                   value = 450,
                   texname = '\\text{MPhiCC}',
                   lhablock = 'MASS',
                   lhacode = [ 8880028 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WZH = Parameter(name = 'WZH',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WZH}',
                lhablock = 'DECAY',
                lhacode = [ 8880023 ])

WWH = Parameter(name = 'WWH',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WWH}',
                lhablock = 'DECAY',
                lhacode = [ 8880024 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WHve = Parameter(name = 'WHve',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WHve}',
                 lhablock = 'DECAY',
                 lhacode = [ 8880012 ])

WHvm = Parameter(name = 'WHvm',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WHvm}',
                 lhablock = 'DECAY',
                 lhacode = [ 8880014 ])

WHvt = Parameter(name = 'WHvt',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WHvt}',
                 lhablock = 'DECAY',
                 lhacode = [ 8880016 ])

WHe = Parameter(name = 'WHe',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WHe}',
                lhablock = 'DECAY',
                lhacode = [ 8880011 ])

WHmu = Parameter(name = 'WHmu',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WHmu}',
                 lhablock = 'DECAY',
                 lhacode = [ 8880013 ])

WHta = Parameter(name = 'WHta',
                 nature = 'external',
                 type = 'real',
                 value = 5,
                 texname = '\\text{WHta}',
                 lhablock = 'DECAY',
                 lhacode = [ 8880015 ])

WHu = Parameter(name = 'WHu',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WHu}',
                lhablock = 'DECAY',
                lhacode = [ 8880002 ])

WHc = Parameter(name = 'WHc',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WHc}',
                lhablock = 'DECAY',
                lhacode = [ 8880004 ])

WHt = Parameter(name = 'WHt',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WHt}',
                lhablock = 'DECAY',
                lhacode = [ 8880006 ])

WHd = Parameter(name = 'WHd',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WHd}',
                lhablock = 'DECAY',
                lhacode = [ 8880001 ])

WHs = Parameter(name = 'WHs',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WHs}',
                lhablock = 'DECAY',
                lhacode = [ 8880003 ])

WHb = Parameter(name = 'WHb',
                nature = 'external',
                type = 'real',
                value = 5,
                texname = '\\text{WHb}',
                lhablock = 'DECAY',
                lhacode = [ 8880005 ])

WHTodd = Parameter(name = 'WHTodd',
                   nature = 'external',
                   type = 'real',
                   value = 5,
                   texname = '\\text{WHTodd}',
                   lhablock = 'DECAY',
                   lhacode = [ 8880007 ])

WHTeven = Parameter(name = 'WHTeven',
                    nature = 'external',
                    type = 'real',
                    value = 5,
                    texname = '\\text{WHTeven}',
                    lhablock = 'DECAY',
                    lhacode = [ 8880008 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WPhi0 = Parameter(name = 'WPhi0',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{WPhi0}',
                  lhablock = 'DECAY',
                  lhacode = [ 8880025 ])

WPhiP = Parameter(name = 'WPhiP',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{WPhiP}',
                  lhablock = 'DECAY',
                  lhacode = [ 8880026 ])

WPhiC = Parameter(name = 'WPhiC',
                  nature = 'external',
                  type = 'real',
                  value = 5,
                  texname = '\\text{WPhiC}',
                  lhablock = 'DECAY',
                  lhacode = [ 8880027 ])

WPhiCC = Parameter(name = 'WPhiCC',
                   nature = 'external',
                   type = 'real',
                   value = 5,
                   texname = '\\text{WPhiCC}',
                   lhablock = 'DECAY',
                   lhacode = [ 8880028 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(244.518*cmath.sqrt(1 + R**2))/(F*R*cmath.acos(1 - 60516/F**2))',
                 texname = '\\text{lam2}')

xL = Parameter(name = 'xL',
               nature = 'internal',
               type = 'real',
               value = 'R**2/(1 + R**2)',
               texname = '\\text{xL}')

d2 = Parameter(name = 'd2',
               nature = 'internal',
               type = 'real',
               value = '-0.8333333333333334 + 2*(1 - xL)*xL + xL**2/2.',
               texname = '\\text{d2}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

lamphi2phi2 = Parameter(name = 'lamphi2phi2',
                        nature = 'internal',
                        type = 'real',
                        value = '-16*lam2**2*R**2',
                        texname = '\\text{lamphi2phi2}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vSM = Parameter(name = 'vSM',
                nature = 'internal',
                type = 'real',
                value = '(160.77*sw)/ee',
                texname = '\\text{vSM}')

xH = Parameter(name = 'xH',
               nature = 'internal',
               type = 'real',
               value = '(5*g1*gw)/(4.*(-g1**2 + 5*gw**2))',
               texname = '\\text{xH}')

g1I = Parameter(name = 'g1I',
                nature = 'internal',
                type = 'real',
                value = 'g1*cmath.sqrt(2)',
                texname = '\\text{g1I}')

gwI = Parameter(name = 'gwI',
                nature = 'internal',
                type = 'real',
                value = 'gw*cmath.sqrt(2)',
                texname = '\\text{gwI}')

lamphi4 = Parameter(name = 'lamphi4',
                    nature = 'internal',
                    type = 'real',
                    value = '(-8*(g1**2 + gw**2))/3. + (16*lam2**2*R**2)/3.',
                    texname = '\\text{lamphi4}')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '(F*cmath.acos(1 - vSM**2/F**2))/cmath.sqrt(2)',
              texname = 'v')

sH = Parameter(name = 'sH',
               nature = 'internal',
               type = 'real',
               value = '(vSM**2*xH)/F**2',
               texname = '\\text{sH}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*v**2)',
                texname = '\\text{lam}')

lamphi2 = Parameter(name = 'lamphi2',
                    nature = 'internal',
                    type = 'real',
                    value = '(2*MH**2)/v**2',
                    texname = '\\text{lamphi2}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/v',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/v',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/v',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/v',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/v',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/v',
                texname = '\\text{yup}')

cH = Parameter(name = 'cH',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sH**2)',
               texname = '\\text{cH}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*v**2)',
                texname = '\\mu')

lamhphiphih = Parameter(name = 'lamhphiphih',
                        nature = 'internal',
                        type = 'real',
                        value = '(-4*lamphi2)/3.',
                        texname = '\\text{lamhphiphih}')

