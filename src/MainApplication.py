from Interpreter import Interpreter
from Utils import Utils

class MainApplication:

    def __init__(self):
        self.utils = Utils()

    def readPromptFileAndReturnList(self, filepath):
        result = []
        data = self.utils.readFromInputFile(filepath)
        for line in data:
            result.append(line.strip().strip('\n'))
        return result

    def executeMethodForObject(self, object, commandList):
        object.readInputFile('../resources/Sample inputPS7.txt')
        object.showAll()
        for val in commandList:
            if('searchLanguage' in val):
                arr = val.split(':')
                object.displayCandidates(arr[1].strip())
            elif('DirectTranslate' in val):
                arr = val.split(':')
                object.findDirectTranslator(arr[1].strip(), arr[2].strip())
            elif('TransRelation' in val):
                arr = val.split(':')
                object.findTransRelation(arr[1].strip(), arr[2].strip())
            else:
                print('invalid command')


if __name__ == '__main__':
    ob = MainApplication()
    commandList = ob.readPromptFileAndReturnList('../resources/Sample promptsPS7.txt')
    ob.executeMethodForObject(Interpreter(), commandList)
