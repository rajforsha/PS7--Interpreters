"""
This is the util class which has 2 method
writeToOutputFile
readFromInputFile
"""
class Utils:

    def __init__(self):
        self.filepath = '../resources/Sample outputPS7.txt'

    # Given a list, writes to file
    def writeToOutputFile(self, data):
        with open(self.filepath, 'a') as file:
            for line in data:
                file.write(line + '\n')
            file.write('\n\n')
            file.close()

    # reads the contents from the file and return as list
    def readFromInputFile(self, filepath):
        data = None
        with open(filepath) as file:
            data = file.readlines()
        file.close()
        return data