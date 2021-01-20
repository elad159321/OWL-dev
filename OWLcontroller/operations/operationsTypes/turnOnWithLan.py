import socket
import subprocess
import platform
from operations.operation import operation

class turnOnWithLan(operation):


    def getKey(self):
        ''' Returns operation's name '''
        return (type(self).__name__)

    @staticmethod
    def pingIP(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
            return False


    @staticmethod
    def runOp(HOST_NAME = '10.100.102.14',MAC_ADRESS = b'\x10\x65\x30\x2B\xE5\x87'):
        # pinging the host for checking if its on
        currentIpAdress = [HOST_NAME]
        for each in currentIpAdress:
            if turnOnWithLan.pingIP(each):
                print(f"{each} Host Pc is available")
            else:
                print(f"{each}  HOST Pc is not available")
                # wake on lan
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(b'\xff' * 6 + MAC_ADRESS * 16,  #Host Pc MAC adress
                         (HOST_NAME, 80)) # Host Pc IP
                # Wake on lan Working


turnOnWithLan.runOp()