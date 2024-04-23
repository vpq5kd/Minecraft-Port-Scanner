
#Imports:
import csv
import socket

class IPFileParse:
    def __init__(self):
        self.filePath = "C:\\Users\\Smspaner\\PycharmProjects\\MCPortScan\\IP2LOCATION-LITE-DB1.CSV"
        self.outFilePath = "parsedIP.CSV"

    """ 'private' method that executes the parse logic. """
    def _read_file(self,country_code):
        ip_array = []
        with open(self.filePath, 'r') as inputFile:
            reader = csv.reader(inputFile)
            for row in reader:
                if row[2] == country_code:
                    ip_array.append(row)
        self._clean_file()
        with open(self.outFilePath, 'a+') as outPutFile:
            for each in ip_array:
                outPutFile.write(','.join(each) + '\n')
    """ 'private' method that erases the out-file each time parse is called."""
    def _clean_file(self):
        with open(self.outFilePath, "w") as file:
            pass

    """method to allow the user to select IP ranges for a certain country code"""
    def parse(self, country_code):
        country_code.upper()
        self._read_file(country_code)

    """method to be called after parse(), translates the ranges into a list of ips
    based on the amount of rows the user wants. Currently this is a VERY inefficient way of finding
    potential 'targets'. future updates will allow more narrow searching for a more efficient system.
    Users may either add a select number of rows or type 'all' to get every ip."""
    def get_ips(self,number_of_rows):
        ip_array = []
        with open(self.outFilePath, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if number_of_rows != "all":
                    if i != number_of_rows:
                        continue
                for j in range(int(row[0]), int(row[1])+1):
                    ip_address = socket.inet_ntoa(bytes.fromhex('{:08x}'.format(j)))
                    ip_array.append(ip_address)
                    # print(ip_address)
        return ip_array

# def main():
#     parser = IPFileParse()
#     parser.parse("US")
#     print(parser.get_ips())
# main()


