
<h2>Modem Scripts:</h2>
<b>the gist</b>

Scripts used to enable and crontrol the Ublox LARA-R203 modem.
Running this command will powerup the onboard modem
This allows testing of the PPP dialer using pon and poff commands to establish
a PPP session.

Provisioning Steps:
First we need to enable serial0. By default the current version of Raspbian comes with this disabled. This needs to be modified in two places.

<b>Install</b>

```
sudo ./setup 10569.mcs ttyAMA0
```
<b>Enabling serial0:</b>
```
# Navigate to the boot folder under root cd /boot
# 1.) Modify the cmdline.txt and change the console parameter from seril0 to tty1
console=tty1

# 2.) Enable serial0 by adding the enable_uart entry to the end of config.txt
enable_uart=1
```
Example:
Login to the pi on three separate terminals

1st Terminal (Logging):
```
tail -f /var/log/ppp.log
```

2nd Terminal (Enalbe Hardware)
```
cd ~/ublox_ppp_dialer
chmod +x ./ppp-creator.sh
sudo ./ppp-creator.sh your-apn-name ttyAMA0
```

3rd Terminal (PPP Dialer)
```
sudo pon gprs # launch hspa-kore script
or
sudo pon gprs # launch hspa-kore script&;

sudo poff gprs# kill hspa-kore script
```
4th (Optional)n Add route so we can ssh through the ppp0 connection
(This can be added to /etc/ppp/ip-up.d/addroute)
```
sudo route add default dev ppp0
```
<b>enable.py</b>

Script used to enable the modem hardware.

Example:
```python
sudo python ublox_lara_r2/enable.py
```

<b>systemd</b>

Commands used to setup systemd service
Example:
```python
sudo python ublox_lara_r2/enable.py

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
