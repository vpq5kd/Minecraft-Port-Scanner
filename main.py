import sys
import socket
import pyfiglet
import IPParser

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






main()


