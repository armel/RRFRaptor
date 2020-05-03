#!/bin/sh
echo "+---------------------------+"
echo "Step 1 - Some apt-get install"
echo "+---------------------------+"
apt-get -y python3-pip
echo "+-----------------------+"
echo "Step 2 - Some pip install"
echo "+-----------------------+"
pip3 install requests
echo "+----------------------+"
echo "Step 3 - Patch Logic.tcl"
echo "+----------------------+"
mv /usr/share/svxlink/events.d/local/Logic.tcl /usr/share/svxlink/events.d/local/Logic.tcl.bak
cp /opt/RRFRaptor/Logic.tcl /usr/share/svxlink/events.d/local/Logic.tcl
echo "+------------------+"
echo "Step 4 - Rock'n roll"
echo "+------------------+"