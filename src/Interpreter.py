class InterPreter:

    def __init__(self):
        self.vertices = [] #list containing languages and interpreter
        self.edges = {} #adjency matrix of edges linking interpreters to languages
        self.interpreters = [] #need to maintain since vertices contain both the langauge and interpreter

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
        with open(filepath) as f:
            lines = f.readlines()
            for line in lines:
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
        for key,val in self.edges.items():
            print(key, val)

    def showAll(self):
        print('--------Function showAll--------')

        print('Total no. of candidates: ', len(self.interpreters))
        print('Total no. of languages: ', len(self.getAllLanguages()))

        print('List of candidates:')
        for candidate in self.interpreters:
            print(candidate)

        print('List of languages:')

        for language in self.getAllLanguages():
            print(language)

    # def displayHireList(self):

if __name__ == '__main__':
    ob = InterPreter()
    ob.readInputFile('../resources/Sample inputPS7.txt')
    ob.showAll()
    ob.printGraph()
    # ob.displayHireList()