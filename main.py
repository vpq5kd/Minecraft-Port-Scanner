import sys
import socket
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
    #prints banner
    banner = pyfiglet.figlet_format("Minecraft Port Scanner")
    print(banner)

    #parses data for us countries
    parser = IPParser.IPFileParse()
    parser.parse("US")

    #gets a list of ips to test
    ip_addresses = parser.get_ips(1)
    #ip_addresses = ["play.neocubest.com","play.vulengate.com","google.com"] #two known and one unknown to demonstrate functionality

    #prints ip addresses with open minecraft ports
    ip_scan = portScan.portScan(ip_addresses)
    ip_scan.thread_scan()







main()


