import os
import time
from operations.operation import operation
PING = 'ping '
#SHUTDOWN_COMMAND = "shutdown command request from client"
SHUTDOWN_COMMAND = "shutdown /s /t 1"

class powerOnWithClicker(operation):
    CLICKER_CHANNEL_COMMANDS ={1 : ('1', 'q'),
                             2 : ('2', 'w'),
                             3 : ('3', 'e'),
                             4 : ('4', 'r')}
    def getKey(self):
        ''' Returns operation's name '''
        return (type(self).__name__)

    @staticmethod
    def runOp(opParams):
        os.system("echo " + powerOnWithClicker.CLICKER_CHANNEL_COMMANDS[opParams.channel][0] + " > " + opParams.com)
        time.sleep(0.5)
        os.system("echo " + powerOnWithClicker.CLICKER_CHANNEL_COMMANDS[opParams.channel][1] + " > " + opParams.com)

        #check if the host turned on
        pingCommand = PING + opParams.hostIP
        while (os.system(pingCommand)) != 0:
            print ("Host is not  alive")
        if (os.system(pingCommand)) == 0:
            print ("host is up")

        return True
# powerOnWithClicker.runOp('COM4', 1)
# powerOnWithClicker.runOp('COM4', 2)
# powerOnWithClicker.runOp('COM4', 3)
# powerOnWithClicker.runOp('COM4', 4)

