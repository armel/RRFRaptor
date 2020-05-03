#!/bin/sh
echo "+---------------------------+"
echo "Step 1 - Some apt-get install"
echo "+---------------------------+"
apt-get -y python3-pip
echo "+-----------------------+"
echo "Step 2 - Some pip install"
echo "+-----------------------+"
pip3 install requests
echo "+------------------+"
echo "Step 3 - Rock'n roll"
echo "+------------------+"