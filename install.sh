
#--font--colors--
green='\033[1;92m'
yellow='\033[1;93m'
red='\033[1;91m'
white='\033[1;97m'
cyan='\033[1;96m'


echo "$yellow
=================================
      Created By Htr-Tech
================================="
echo ""
echo ""
echo "$green
====================================
   Installing termux login script
===================================="

echo "$yellow 
================================
    Installing packages
================================"
apt update
apt install python -y
apt install ruby -y
gem install lolcat
echo "green
======================
        Done
======================"
echo ""
echo ""
echo "
======================
    Initializing...
======================"
rm $PREFIX/etc/bash.bashrc
cd core
cp bash.bashrc $PREFIX/etc
cp login_script.py $PREFIX/etc
echo "green
======================
        Done
======================"
clear
echo "$yellow
=================================
      Created By Htr-Tech
================================="
echo "$yellow 
     Instagram : @tahmid.rayat
================================="
echo "$yellow 
     github.com/htr-tech
================================="
echo ""
echo "$green
======================================
  Now type 'exit' & restart Termux
======================================"
echo ""
echo "$white"
