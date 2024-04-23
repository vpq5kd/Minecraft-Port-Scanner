#imports:
import socket
import sys
class portScan:
    def __init__(self,ip_addresses):
        self.ip_addresses = ip_addresses
        self.port = 25565

    """method to scan each ip address for an open minecraft port: 25565 """
    def scan(self):
        try:
            for ip_address in self.ip_addresses:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                result = s.connect_ex((ip_address,self.port))
                print(f'{ip_address}')
                if result == 0:
                    print(f'{ip_address} has an open minecraft port')
        except KeyboardInterrupt:
            print("Program ended")
            sys.exit()
        except socket.gaierror:
            print("host name couldn't be resolved")
            sys.exit()
        except socket.error:
            print("server not responding")
            sys.exit()


