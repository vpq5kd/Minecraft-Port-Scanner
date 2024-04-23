
#Imports:
import csv

class IPFileParse:
    def __init__(self):
        self.filePath = "C:\Users\Smspaner\PycharmProjects\MCPortScan\IP2LOCATION-LITE-DB1.CSV"
    def _read_file(self):
        ip_array = []
        with open(self.filePath, 'r') as inputFile:
            reader = csv.reader(inputFile)
            for row in reader:
                if row[2] == "US":
                    ip_array.append(row)
        with open("parsedIP.CSV", 'a') as outPutFile:
            for each in ip_array:
                outPutFile.write(each)
    def parse(self):
        self._read_file()
        return


