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
    def runOp(hostinfo):

        messegeToServer = {"operation": "shutdown", "param": SHUTDOWN_COMMAND}
        hostinfo.socket.sendall(json.dumps(messegeToServer).encode('utf-8'))  # encode the dict to JSON
        messegeFromServer = hostinfo.socket.recv(1024).decode()  # receive response from the server

        # sending a ping in order to verify the shutdown
        pingCommand = PING + hostinfo.hostIP
        while (os.system(pingCommand)) == 0:
            print ("Host still alive")
        if (os.system(pingCommand)) != 0:
            print ("shoutdown was done")
        return ('Received from server: ' + messegeFromServer)  # show the response in terminal