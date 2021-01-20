from operations.operation import operation
import json
PING = 'ping '
#SLEEP_COMMAND ="sleep command request from client"
SLEEP_COMMAND = 'rundll32.exe powrprof.dll,SetSuspendState 0,1,0'

class sleep(operation):
    def getKey(self):
        pass

    @staticmethod
    def runOp(hostinfo):

        messegeToServer = {"operation": "sleep", "param": SLEEP_COMMAND}
        hostinfo.socket.sendall(json.dumps(messegeToServer).encode('utf-8'))  # encode the dict to JSON

        # sending a ping in order to verify the shutdown
        # pingCommand = PING + host
        # if (os.system(pingCommand)) == 0:
        #     print ("alive")
        return