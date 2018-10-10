import os
from lib_module_lara_r2 import *

def enable_hardware():
    u = UbloxLaraR2()
    u.initialize()
    u.reset_power()

def auto_pon():
    os.system("pon gprs")

if __name__ == "__main__":

    enable_hardware()
    auto_pon()



# # Close debug massage 
# u.debug = True

# # show module name
# if u.sendAT("AT+CGMM\r\n", "OK\r\n"):
#     print "\r\nmodule name: ", u.response.split('\r\n')[1]

# if u.sendAT("AT+CGDCONT?\r\n", "OK\r\n"):
#     print "\r\nCGDCONT: ", u.response.split('\r\n')[1]

# # get SIM card state
# if u.sendAT("AT+CSIM?\r\n", "OK\r\n"):
#     print "\r\nSIM state: ", u.response.split('\r\n')[1]

# # check rssi
# rssi = u.getRSSI()
# print "RSSI: ", rssi
