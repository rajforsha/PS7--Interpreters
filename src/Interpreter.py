from Utils import Utils
class Interpreter:

    def __init__(self):
        self.vertices = [] #list containing languages and interpreter
        self.edges = {} #adjency matrix of edges linking interpreters to languages
        self.interpreters = [] #need to maintain since vertices contain both the langauge and interpreter
        self.utils = Utils()

    def addLanguagesOrInterpreters(self, val):
        val = val.strip()
        if val not in self.vertices:
            self.vertices.append(val)


    def linkInterpretersToLangauages(self, interpreter, language):
        #undirected graph, hence adding to both the ends
        interpreter = interpreter.strip()
        language = language.strip()

        if self.edges.get(interpreter) is None:
            self.edges[interpreter]=[language]
        else:
            self.edges[interpreter].append(language)

        if self.edges.get(language) is None:
            self.edges[language] = [interpreter]
        else:
            self.edges[language].append(interpreter)


    def readInputFile(self, filepath):
        data = self.utils.readFromInputFile(filepath)
        for line in data:
            values = line.strip('\n').split('/')
            name = values[0]
            self.interpreters.append(name.strip())
            self.addLanguagesOrInterpreters(name)
            for i in range(1, len(values)):
                self.linkInterpretersToLangauages(name, values[i])
                self.addLanguagesOrInterpreters(values[i])


    def getAllLanguages(self):
        s1 = set(self.vertices)
        s2 = set(self.interpreters)
        return s1-s2

    def printGraph(self):
        self.utils.writeToOutputFile('--------Function printGraph--------')
        for key,val in self.edges.items():
            self.utils.writeToOutputFile(key, val)

    def showAll(self):
        self.utils.writeToOutputFile('--------Function showAll--------')

        self.utils.writeToOutputFile('Total no. of candidates: ' + str(len(self.interpreters)))
        self.utils.writeToOutputFile('Total no. of languages: '+ str(len(self.getAllLanguages())))

        self.utils.writeToOutputFile('List of candidates:')
        for candidate in self.interpreters:
            self.utils.writeToOutputFile(candidate)

        self.utils.writeToOutputFile('List of languages:')

        for language in self.getAllLanguages():
            self.utils.writeToOutputFile(language)

    def displayCandidates(self, lang):
        list = self.edges.get(lang)
        self.utils.writeToOutputFile('--------Function displayCandidates--------')
        self.utils.writeToOutputFile('List of Candidates who can speak '+ lang +':')
        for candidate in list:
            self.utils.writeToOutputFile(candidate)
