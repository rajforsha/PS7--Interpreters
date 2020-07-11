from Interpreter import Interpreter
from Utils import Utils


# This is the main application class which triggers all the method required for this assignment.
class MainApplication:

    # we are initializing application with the path to input and prompt file.
    def __init__(self):
        self.utils = Utils()
        self.inputFile = './inputPS7.txt'
        self.promptFile = './promptsPS7.txt'

    # we are using out util class to read the inout file and return the contents as lines
    def readPromptFileAndReturnList(self):
        result = []
        data = self.utils.readFromInputFile(self.promptFile)
        for line in data:
            result.append(line.strip().strip('\n'))
        return result

    """
     returns the total number of vertices, reads from the input file and count every entry in a line as vertex
     we need the total count of vertex to initialize our interpreter class with the total count.
    """
    def getTotalvertices(self):
        # need to get total vertices to populate graph
        lines = self.utils.readFromInputFile(self.inputFile)
        result = []
        for line in lines:
            data = line.strip('\n').strip().split('/')
            for val in data:
                result.append(val.strip())
        return len(set(result))

    """
    pre-requisite: we know the count of vertex, now we need to create adjacency matrix, which we doing on line 47
    this is the exceute method, which reads the task from the prompt file and, execute the method from interpreter class
    object : this is the object created for interpreter
    commandList : this is the list containing all the commands we need to execute.
    showMinList
    searchLanguage: Hindi
    DirectTranslate: English : Malayalam
    TransRelation: English : Malayalam
    """
    def executeMethodForObject(self, object, commandList):
        object.readApplications('./inputPS7.txt')
        object.showAll()
        for val in commandList:
            if('showMinList' in val):
                object.displayHireList()
            elif('searchLanguage' in val):
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


"""
we get all the commands ready as list and we also get the total number of vertices
we create an object of interpreter and pass to the execute method.
"""
if __name__ == '__main__':
    ob = MainApplication()
    commandList = ob.readPromptFileAndReturnList()
    ob.executeMethodForObject(Interpreter(ob.getTotalvertices()), commandList)
