#!/bin/sh
echo "+---------------------------+"
echo "Step 1 - Git clone"
echo "+---------------------------+"
rm -rf /opt/RRFRaptor
cd /opt
git clone https://github.com/armel/RRFRaptor.git 
echo "+---------------------------+"
echo "Step 2 - Some apt-get install"
echo "+---------------------------+"
apt-get -y python3-pip
echo "+-----------------------+"
echo "Step 3 - Some pip install"
echo "+-----------------------+"
pip3 install requests
echo "+----------------------+"
echo "Step 4 - Patch Logic.tcl"
echo "+----------------------+"
mv /usr/share/svxlink/events.d/local/Logic.tcl /usr/share/svxlink/events.d/local/Logic.tcl.bak
cp /opt/RRFRaptor/Logic.tcl /usr/share/svxlink/events.d/local/Logic.tcl
echo "+------------------+"
echo "Step 5 - Rock'n roll"
echo "+------------------+"