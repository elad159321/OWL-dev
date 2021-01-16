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
    def runOp(COM, channel):
        os.system("echo "+ powerOnWithClicker.CLICKER_CHANNEL_COMMANDS[channel][0] +" > " + COM)
        time.sleep(0.5)
        os.system("echo "+ powerOnWithClicker.CLICKER_CHANNEL_COMMANDS[channel][1] +" > " + COM)

powerOnWithClicker.runOp('COM4', 1)
powerOnWithClicker.runOp('COM4', 2)
powerOnWithClicker.runOp('COM4', 3)
powerOnWithClicker.runOp('COM4', 4)

