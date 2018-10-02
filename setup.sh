#!/bin/bash

#. /etc/lsb_release
#OS=$DISTRIB_ID
#VER=$DISTRIB_RELEASE

#if [[ "$OS" != "Ubuntu"]] || [[ "$VER" != "14.04" ]]; then
#	echo "Unsupported OS installed!"
#	exit
#fi

echo "Running modemscripts setup..."

apt-get update
apt-get install git
apt-get install ppp
apt-get install python-dev python-pip
pip install wiringpi2
pip install pyserial

#apt-get install openssh-server
#apt-get install expect

#git clone https://github.com/johncobb/modemscripts.git /home/pi/apps/modemscripts

if test -d /etc/ppp/peers; then
	echo "exists";
else
	sudo mkdir /etc/ppp/peers;
	echo "etc/ppp/peers not found. creating...";
fi


# Copy PPP dependencies
sudo cp /home/pi/modemscripts/etc/ppp/options /etc/ppp/options
sudo cp /home/pi/modemscripts/etc/ppp/peers/* /etc/ppp/peers
sudo cp /home/pi/modemscripts/etc/ppp/ip-up.d/addroute /etc/ppp/ip-up.d/addroute

#echo "updating /boot/cmdline.txt"
#cp /boot/cmdline.txt /boot/cmdline.txt.bak
#sed -i -e 's/console=serial0/console=tty0/g' /boot/cmdline.txt
#echo "updating /boot/config.txt"
#cp /boot/config.txt /boot/config.txt.bak
#echo "enable_uart=1" >> /boot/config.txt

#git clone https://github.com/johncobb/modemscripts.git /home/pi/apps/modemscripts

#git clone https://github.com/johncobb/modemscripts.git /home/pi/apps/modemscripts
# copy service descriptor to systemd folder

#sudo cp /home/pi/apps/modemscripts/systemd/enablemodem.service /etc/systemd/system/enablemodem.service

#systemctl enable enablemodem.service
#systemctl start enablemodem.service
#systemctl daemon-reload

#reboot
