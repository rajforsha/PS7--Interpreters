class Utils:

    def __init__(self):
        self.filepath = '../resources/Sample outputPS7.txt'

    def writeToOutputFile(self, data):
        with open(self.filepath, 'a') as file:
            file.write(data + '\n')
            file.close()

    def readFromInputFile(self, filepath):
        data = None
        with open(filepath) as file:
            data = file.readlines()
        file.close()
        return data