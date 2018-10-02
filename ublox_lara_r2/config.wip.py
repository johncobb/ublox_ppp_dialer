import threading
import datetime
import time
import serial


class ModemSettings:
    APN = "10569.mcs"


class Modem(threading.Thread):
    def __init__(self, modemCallbacFunc=None, port='/dev/ttyAMA0', baudrate=115200, *args):
        self._target = self.modem_handler
        self._args = args
        self.closing = False
        self.commands = []
        self.timeout = 0
        self.modemCallback = modemCallbacFunc
        self.modemBusy = False
        self.ser = serial.Serial(port, baudrate)
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)

    def shutdown(self):
        self.closing = True
        if self.ser.isOpen():
            self.ser.close()

    def write(self, cmd):
        self.ser.write(cmd)

    def modem_handler(self):
        tmp_buffer = ""
        
        if(self.ser.isOpen()):
            self.ser.close()


        while not self.closing:

            """ Check to see if there are commands """
            if (len(self.commands) > 0):
                modem_command = self.commands.pop(0)
                self.write(modem_command)
                continue            

            while(self.ser.inWaiting() > 0):
                #print 'modem has data!!!'
                tmp_char = self.ser.read(1)
                if(tmp_char == '\r'):
                    result = self.modem_parse_result(tmp_buffer)
                    print('received ', tmp_buffer)
                    # Make sure we received something worth processing
                    if(result.ResultCode > CpModemResultCode.RESULT_UNKNOWN):
                        #print 'known result code', result
                        if(self.modemCallback != None):
                            self.modemCallback(result)
                            self.modemBusy = False
                    #print 'modem response ', tmp_buffer
                    tmp_buffer= ""
                else:
                    tmp_buffer += tmp_char
                time.sleep(.005)

    def enqueue_command(self, cmd):
        self.modemBusy = True
        self.commands.append(cmd)

    def set_timeout(self, timeout):
        self.timeout = datetime.now() + timeout
    
    def is_timeout(self):
        return (datetime.now() >= self.timeout)

    def is_error(self, token):
        return (token.find("ERROR") > -1)

    def modem_send_at(self, callback):
        self.enqueue_command("AT\r")
        self.modemResponseCallbackFunc = callback
        pass

    def modem_set_echo_off(self, callback):
        self.enqueue_command("ATE0\r")
        self.modemResponseCallbackFunc = callback
        pass

    def modem_set_context(self, callback):
        cmd = "AT+CGDCONT=1,\"IP\",\"%s\"\r" % (ModemSettings.APN)
        self.enqueue_command(cmd)
        self.modemResponseCallbackFunc = callback
        pass

    def modem_qry_context(self, callback):
        self.enqueue_command("AT#SGACT?\r")
        self.modemResponseCallbackFunc = callback
        pass  
    
    def modem_qry_signal(self, callback):
        self.enqueue_command("AT+CSQ?\r")
        self.modemResponseCallbackFunc = callback
        pass   
    
    def modem_qry_network(self, callback):
        self.enqueue_command("AT+CREG?\r")
        self.modemResponseCallbackFunc = callback
        pass     



def modemDataReceived(data):
    print("modemDataReceived", data)


if __name__ == "__main__":
    print("Running...")      
    modemThread = Modem(modemDataReceived, port='/dev/ttyAMA0', baudrate=115200)
    modemThread.start()

    while(modemThread.isAlive()):
        modemThread.modem_send_at(modemDataReceived)

        time.sleep(1)
    
    print("Exiting App...")
    exit()


        
            


        




