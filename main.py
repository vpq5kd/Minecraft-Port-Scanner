import sys
import socket
import threading

import pyfiglet
import IPParser
import portScan

#resources:
"""Port-scan basics: https://www.geeksforgeeks.org/port-scanner-using-python/ """
#credits:
"""MCPortScan uses the IP2Location LITE database for <a href="https://lite.ip2location.com">IP geolocation</a>."""
#token:
"""a2ac8205d5bae3"""


#main:
def main():
    #prints banner (idea from geeks for geeks)
    banner = pyfiglet.figlet_format("Minecraft Port Scanner")
    print(banner)
    print("-" * 50)

    #parses data for us countries
    parser = IPParser.IPFileParse()
    parser.parse("US")

    #gets a list of ips to test
    ip_addresses = parser.get_ips(13000)
    ip_addresses_1 = parser.get_ips(13001)
    ip_addresses_2 = parser.get_ips(13002)
    #ip_addresses = ["play.neocubest.com","play.vulengate.com","google.com"] #two known and one unknown to demonstrate functionality

    #prints ip addresses with open minecraft ports
    # ip_scan = portScan.portScan(ip_addresses)
    # ip_scan.thread_scan()

    """ attempt at multi-threading to further increase efficiency (STILL WORKING): """

    ip_scan_0 = portScan.portScan(ip_addresses)
    ip_scan_1 = portScan.portScan(ip_addresses_1)
    ip_scan_2 = portScan.portScan(ip_addresses_2)

    ip_scans = [ip_scan_0, ip_scan_1, ip_scan_2]
    threads = []
    for ip_scan in ip_scans:
        t = threading.Thread(target=ip_scan.thread_scan())
        threads.append(t)
        t.start()
    for t in threads:
        t.join()




main()


