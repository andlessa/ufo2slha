#!/bin/sh

homeDIR="$( pwd )"



madgraph="MG5_aMC_v2.6.2.tar.gz"
URL=https://launchpad.net/mg5amcnlo/2.0/2.6.x/+download/$madgraph
echo -n "Install MadGraph (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir MG5;
if [ ! -f $madgraph ]; then
    echo "[installer] getting MadGraph5"; wget $URL 2>/dev/null || curl -O $URL; 
fi

	tar -zxf $madgraph -C MG5 --strip-components 1;
	cd $homeDIR
	echo "[installer] replacing MadGraph files with fixes";
    cp ./madgraphFixes/mg5_configuration.txt MG5/input/;
    cp ./madgraphFixes/madgraph_interface.py MG5/madgraph/interface/;
    cp ./madgraphFixes/common_run_interface.py MG5/madgraph/interface/;
    cp ./madgraphFixes/diagram_generation.py MG5/madgraph/core/;

    currentver="$(gcc -dumpversion)"
    requiredver="7"
    if [ "$(printf '%s\n' "$requiredver" "$currentver" | sort -V | head -n1)" = "$requiredver" ]; then 
        echo "GCC version is greater than 7. Please install gcc-7, gfortran-7 and libstdc++-7-dev."
        cp ./madgraphFixes/mg5_configuration7.txt MG5/input/mg5_configuration.txt;    
    fi

fi



echo "DONE"
