from Interpreter import Interpreter

class MainApplication:

    def __init__(self):
        print('MainApplication')

    def readPromptFileAndReturnList(self, filepath):
        result = []
        with open(filepath) as f:
            lines = f.readlines()
            for line in lines:
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
                print('DirectTranslate')
            elif('TransRelation' in val):
                print('TransRelation')
            else:
                print('invalid command')


if __name__ == '__main__':
    ob = MainApplication()
    commandList = ob.readPromptFileAndReturnList('../resources/Sample promptsPS7.txt')
    ob.executeMethodForObject(Interpreter(), commandList)
