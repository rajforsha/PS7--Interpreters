from Interpreter import Interpreter
from Utils import Utils

class MainApplication:

    def __init__(self):
        self.utils = Utils()
        self.inputFile = '../resources/Sample inputPS7.txt'
        self.promptFile = '../resources/Sample promptsPS7.txt'

    def readPromptFileAndReturnList(self):
        result = []
        data = self.utils.readFromInputFile(self.promptFile)
        for line in data:
            result.append(line.strip().strip('\n'))
        return result

    def getTotalvertices(self):
        # need to get total vertices to populate graph
        lines = self.utils.readFromInputFile(self.inputFile)
        result = []
        for line in lines:
            data = line.strip('\n').strip().split('/')
            for val in data:
                result.append(val.strip())
        return len(set(result))

    def executeMethodForObject(self, object, commandList):
        object.populateAdjacencyMatrixFromInputFile('../resources/Sample inputPS7.txt')
        # object.showAll()
        object.printGraph()
        # for val in commandList:
        #     if('showMinList' in val):
        #         object.displayHireList()
        #     elif('searchLanguage' in val):
        #         arr = val.split(':')
        #         object.displayCandidates(arr[1].strip())
        #     elif('DirectTranslate' in val):
        #         arr = val.split(':')
        #         object.findDirectTranslator(arr[1].strip(), arr[2].strip())
        #     elif('TransRelation' in val):
        #         arr = val.split(':')
        #         object.findTransRelation(arr[1].strip(), arr[2].strip())
        #     else:
        #         print('invalid command')


if __name__ == '__main__':
    ob = MainApplication()
    commandList = ob.readPromptFileAndReturnList()
    ob.executeMethodForObject(Interpreter(ob.getTotalvertices()), commandList)
