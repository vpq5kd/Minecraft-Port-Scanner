
#Imports:
import csv

class IPFileParse:
    def __init__(self):
        self.filePath = "C:\\Users\\Smspaner\\PycharmProjects\\MCPortScan\\IP2LOCATION-LITE-DB1.CSV"
        self.outFilePath = "parsedIP.CSV"
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
    def _clean_file(self):
        with open(self.outFilePath, "w") as file:
            pass
    def parse(self, country_code):
        country_code.upper()
        self._read_file(country_code)
def main():
    parser = IPFileParse()
    parser.parse("US")
main()


