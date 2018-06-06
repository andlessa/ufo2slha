#!/bin/sh

homeDIR="$( pwd )"



madgraph="MG5_aMC_v2.6.2.tar.gz"
URL=https://launchpad.net/mg5amcnlo/2.0/2.6.x/+download/$madgraph
echo -n "Install MadGraph (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir MG5;
	echo "[installer] getting MadGraph5"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $madgraph -C MG5 --strip-components 1;
	cd $homeDIR
	rm $madgraph;
	echo "[installer] replacing MadGraph files with fixes";
    cp ./madgraphFixes/mg5_configuration.txt MG5/input/;
    cp ./madgraphFixes/madgraph_interface.py MG5/madgraph/interface/;
    cp ./madgraphFixes/common_run_interface.py MG5/madgraph/interface/;
    cp ./madgraphFixes/diagram_generation.py MG5/madgraph/core/;
fi

echo "DONE"
