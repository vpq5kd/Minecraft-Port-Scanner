#imports:
import socket
import sys
import threading
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
                print(f'scanning {ip_address}')
                if result == 0:
                    print(f'{ip_address} has an open minecraft port')
                else:
                    print(f"{ip_address} doesn't have an open minecraft port")
        except KeyboardInterrupt:
            print("Program ended")
            sys.exit()
        except socket.gaierror:
            print("host name couldn't be resolved")
            sys.exit()
        except socket.error:
            print("server not responding")
            sys.exit()

    """trial-method to see if using threads would make the broader scan more
    efficient. I used chat-gpt3.5 to aid in my understanding of python-threading."""
    def thread_scan(self):
        threads = []
        for ip_address in self.ip_addresses:
            t = threading.Thread(target=self._thread_scan_logic, args=(ip_address))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

    """copy of the scan() method but instead it only takes on ip address as an argument"""
    def _thread_scan_logic(self, ip_address):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((ip_address,self.port))
            print(f'scanning {ip_address}')
            if result == 0:
                print(f'{ip_address} has an open minecraft port')
            else:
                print(f"{ip_address} doesn't have an open minecraft port")
        except KeyboardInterrupt:
            print("Program ended")
            sys.exit()
        except socket.gaierror:
            print("host name couldn't be resolved")
            sys.exit()
        except socket.error:
            print("server not responding")
            sys.exit()


