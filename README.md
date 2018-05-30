# ufo2slha
This repository holds the code for producing slha files from UFO files


## Basic Installation ##

The following external codes are required:

  * [MadGraph](https://sarah.hepforge.org/)

The script installer.sh will try to fetch the appropriate tarballs and try to install them.


### Generating SLHA files ###

The cross-sections for the MSSM scenario can be computed as usual with smodelsTools.py.
However, for the IDM model MadGraph5 must be used. Running:

``
./runGetXSecs.py -p <parameter file>
`` 

will use the parameters defined in the parameter file (see example in [xsec_parameters.ini](xsec_parameters.ini))
and run MG5 to compute the cross-sections (using the processes defined in [proc_card.dat](inputCards/proc_card.dat)).
The results will be used to generate a SLHA file with cross-sections, which can then be used as input to SModelS.

