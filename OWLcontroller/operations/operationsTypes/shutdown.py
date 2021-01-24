import os
from operations.operation import operation
import json
PING = 'ping '
#SHUTDOWN_COMMAND = "shutdown command request from client"
SHUTDOWN_COMMAND = "shutdown /s /t 1"
class shutdown(operation):
    def getKey(self):
        pass

    @staticmethod
    def runOp(opParams):

        messegeToServer = {"operation": "shutdown", "param": SHUTDOWN_COMMAND}
        opParams.socket.sendall(json.dumps(messegeToServer).encode('utf-8'))  # encode the dict to JSON
        opParams.socket.close()

        # sending a ping in order to verify the shutdown
        pingCommand = PING + opParams.hostIP
        while (os.system(pingCommand)) == 0:
            print ("Host still alive")
        if (os.system(pingCommand)) != 0:
            print ("shoutdown was done")
            opParams.socket.close()
            return True