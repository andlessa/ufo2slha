# ufo2slha
This repository holds the code for producing a SLHA file from the Little(st) Higgs UFO input model.

## Basic Installation ##

The following external codes are required:

  * [MadGraph](https://launchpad.net/mg5amcnlo)

The script installer.sh will try to fetch the appropriate tarballs and install them.
A few patches will be automatically applied to the MadGraph installation in order to allow for the automatized computation
of cross-sections. *Therefore we do not recommend to use an external MadGraph installation.*
The patched files can be found in [madgraphFixes](madgraphFixes).


### Generating SLHA files ###

A SLHA file for any input model and set of parameters can be 
obtained running:

``
./createSLHA.py -p <parameter file>
`` 

The parameter file specificies several options for computing the cross-sections and the decays.
An example with comments can be found in [slha_parameters.ini](slha_parameters.ini).
Note that generating SLHA files for several model parameters can be automatically
done by defining the corresponding parameters using the [$loop{}](slha_parameters.ini#L20) syntax. Also, dependence between the parameters
are easily implemented using the parameter variable syntax [${option}](slha_parameters.ini#L21)
to reference options in the same section or [${section:option}](slha_parameters.ini#L24)
to reference options in a different section (see comments in [slha_parameters.ini](slha_parameters.ini) and a more complex example in [lhiggs_parameters.ini](lhiggs_parameters.ini)).

Note that the automatic computation of cross-sections for all possible
cross-section channels may demand a lot of CPU time. Therefore we recommend the user
to judisciously choose which particles to compute cross-sections for and, if needed,
explicitly specify the required processes through the use of the process
card (see comments in [slha_parameters.ini](slha_parameters.ini)).

#### SLHA creation Steps ####

The creation of an SLHA file from the UFO input is done according to the following steps:
  1. If a process card is defined and it already exists (see proccard in [slha_parameters.ini](slha_parameters.ini)), 
     this file will be used to generate the madgraph processes. Otherwise
     a process card will be autmatically created to generate all p p -> 2 processes using the particles listed in computeXsecsFor.
     The output will be saved  to the process folder 
     (defined by processFolder in [slha_parameters.ini](slha_parameters.ini)). If the process folder
     already exists, the process generation will be skipped.
  2. Once the information about the processes are stored in the process folder (see above), this folder will be copied
     to the madgraph output folder (see mg5out in [slha_parameters.ini](slha_parameters.ini)). When creating several SLHA
     files in parallel, it is important to assign one distinct mg5out folder for each SLHA file (if cleanOutFolders = True, these
     folders will be automatically removed at the end of the run).
  3. Events will then be generated using the parameters set by the "MadGraphSet" section in  [slha_parameters.ini](slha_parameters.ini)
     and the run and parameter cards defined by the runcard and paramcard options. If these are not defined or the files
     do not exist, the default files will be used.
  4. Finally the LHE event file generated by madgraph (specified as the ''inputFile'' option in the ''slhaCreator'' section 
     in  [slha_parameters.ini](slha_parameters.ini)) will be read and used to extract the cross-sections and the other SLHA blocks, which will then
     be written to the output SLHA file (defined by the ''slhaout'' option in the "slhaCreator" section 
     in  [slha_parameters.ini](slha_parameters.ini))
  5. If cleanOutFolders = True, the madgraph output folder(s) will be deleted.


