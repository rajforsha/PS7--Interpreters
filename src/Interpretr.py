class InterPretr:

    def __init__(self):
        self.vertices = [] #list containing languages and interpreter
        self.edges = {} #adjency matrix of edges linking interpreters to languages

    def addLanguagesOrInterpreters(self, val):
        val = val.strip()
        if val not in self.vertices:
            self.vertices.append(val)


    def linkInterpretersToLangauages(self, interpreter, language):
        interpreter = interpreter.strip()
        language = language.strip()
        if self.edges.get(interpreter) is None:
            self.edges[interpreter]=[language]
        else:
            self.edges[interpreter].append(language)

    def readInputFile(self, filepath):
        with open(filepath) as f:
            lines = f.readlines()
            for line in lines:
                values = line.strip('\n').split('/')
                name = values[0]
                self.addLanguagesOrInterpreters(name)
                for i in range(1, len(values)):
                    self.linkInterpretersToLangauages(name, values[i])
                    self.addLanguagesOrInterpreters(values[i])

    def showAll(self):
        print('--------Function showAll--------')
        print('Total no. of candidates: ', len(self.edges.keys()))
        s1 = set(self.vertices)
        s2 = set(self.edges.keys())

        print('Total no. of languages: ', len(s1-s2))

        print('List of candidates:')
        for candidate in s2:
            print(candidate)

        languages = s1-s2

        print('List of languages:')

        for language in languages:
            print(language)


    def print(self):
        print('-----------vertices are -----------')
        print(self.vertices)
        print('--------------edges are ------------')
        print(self.edges)




if __name__ == '__main__':
    ob = InterPretr()
    ob.readInputFile('../resources/Sample inputPS7.txt')
    ob.showAll()