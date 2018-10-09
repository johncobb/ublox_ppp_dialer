
<h2>Ublox PPP Dialer:</h2>
<b>Setup</b>

ublox_ppp_dialer is used to enable and establish a PPP connection with the Ublox LARA-R203 modem.
Running setup.sh will configure the Raspberry Pi with the settings and scripts necessary to establish and maintain 
a PPP connection.

<b>Getting Started:</b>

To use the LARA-R203 modem hat we need to configuire the device tree overlay to enable UART0 on the Raspberry Pi3. We
do this by adding the following ```dtoverlay=pi3-disalbe-bt``` to the ```/boot/config.txt```. Next disable the hciuart in system service. This is done by issuing the following command: ```sudo systemctl disable hciuart```. Next, we need to remove the ```console=serial0,115200``` from ```/boot/cmdline.txt``` to disable console output on serial0. Finally reboot the Pi and we are ready to communicate with the modem.

All of these tasks are handled in the ```setup.sh``` script documented below. Simply run the script and reboot; the Pi will establish a PPP connnection when it boots up.

<b>Install</b>
```
git clone https://github.com/ublox_ppp_dialer.git
cd ~/ublox_ppp_dialer
chmod +x ./setup.sh
sudo ./setup.sh your-apn-name ttyAMA0
```

<b>Debugging:</b>

Login to the Pi from three separate terminal sessions or establish multiple screens to toggle between.

1st Terminal (Logging):
```
tail -f /var/log/ppp/log

# if PPP connection was successful you should see something similar to the following

rcvd [IPCP ConfReq id=0x2 <addr 10.204.254.143>]
sent [IPCP ConfAck id=0x2 <addr 10.204.254.143>]
rcvd [IPCP ConfAck id=0x2 <addr 10.204.254.143> <ms-dns1 174.47.40.106> <ms-dns2 174.47.20.106>]
not replacing default route to wlan0 [10.0.0.1]
local  IP address 10.204.254.143
remote IP address 10.204.254.143
primary   DNS address 174.47.40.106
secondary DNS address 174.47.20.106
Script /etc/ppp/ip-up started (pid 538)
Script /etc/ppp/ip-up finished (pid 538), status = 0x0

```

2nd Terminal (Enable Hardware)
```
cd ~/ublox_ppp_dialer
chmod +x ./setup.sh
sudo ./setup.sh your-apn-name ttyAMA0
reboot
```

3rd Terminal (PPP Session)
```
ifconfig ppp0
```
4th (Optional)n Add route so we can ssh through the ppp0 connection
(This can be added to /etc/ppp/ip-up.d/addroute)
```
sudo route add default dev ppp0
```
<b>Troubleshooting systemd</b>

The following commands can be used to configure and troubleshoot systemd:
```
# setting up service
systemctl enable enablemodem.service
systemctl start enablemodem.service
systemctl daemon-reload

# disabling service
sudo systemctl disable enablemodem.service

# checking status
sudo systemctl status enablemodem.service
sudo systemctl is-active enablemodem.service
sudo systemctl is-enabled enablemodem.service
sudo systemctl is-failed enablemodem.service
sudo systemctl disable enablemodem.service
```
