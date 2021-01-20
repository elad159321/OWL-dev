import os
CMD_COMMAND = 'cmd /k '

class shutdown(object):
    def __init__(self):
        pass

    def getKey(self):
        ''' Returns operation's name '''
        return (type(self).__name__)

    @staticmethod
    def runOp(userCommand):
        print(userCommand)
        #return userCommand in case we are checking it on the same pc (in order to nu shoutdown the PC)
        os.system("shutdown /s /t 1")