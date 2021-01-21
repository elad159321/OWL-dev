import os
import time
from operations.operation import operation


class powerOnWithClicker(operation):
    CLICKER_CHANNEL_COMMANDS ={1 : ('1', 'q'),
                             2 : ('2', 'w'),
                             3 : ('3', 'e'),
                             4 : ('4', 'r')}
    def getKey(self):
        ''' Returns operation's name '''
        return (type(self).__name__)

    @staticmethod
    def runOp(hostinfo):
        os.system("echo "+ powerOnWithClicker.CLICKER_CHANNEL_COMMANDS[hostinfo.channel][0] +" > " + hostinfo.com)
        time.sleep(0.5)
        os.system("echo "+ powerOnWithClicker.CLICKER_CHANNEL_COMMANDS[hostinfo.channel][1] +" > " + hostinfo.com)
        return True
# powerOnWithClicker.runOp('COM4', 1)
# powerOnWithClicker.runOp('COM4', 2)
# powerOnWithClicker.runOp('COM4', 3)
# powerOnWithClicker.runOp('COM4', 4)

