#!/bin/sh

homeDIR="$( pwd )"



madgraph="MG5_aMC_v3.5.2.tar.gz"
URL=https://launchpad.net/mg5amcnlo/2.0/2.5.x/+download/$madgraph
echo -n "Install MadGraph (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir MG5;
if [ ! -f $madgraph ]; then
    echo "[installer] getting MadGraph5"; wget $URL 2>/dev/null || curl -O $URL; 
fi

	tar -zxf $madgraph -C MG5 --strip-components 1;
	cd $homeDIR
fi


echo "DONE"
