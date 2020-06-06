from Utils import Utils
class Interpreter:

    def __init__(self, vertices):
        self.vertices = vertices #list containing languages and interpreter
        self.edges = [ [ None for i in range(vertices) ] for j in range(vertices) ] #adjency matrix of edges linking interpreters to languages
        self.interpreters = [] #need to maintain since vertices contain both the langauge and interpreter
        self.mapping = {} #mapping vertices to integer value
        self.utils = Utils()

    def addEdges(self, src, dest):
        #undirected graph, hence adding to both the ends
        self.edges[src][dest] = 1
        self.edges[dest][src] = 1


    def populateAdjacencyMatrixFromInputFile(self, filepath):
        data = self.utils.readFromInputFile(filepath)
        index = 0 #used for mapping
        for line in data:
            values = line.strip('\n').split('/')
            name = values[0].strip() #first word
            self.mapping[name]= index
            self.mapping[index] = name
            self.interpreters.append(name) #need to track interpreters
            index += 1
            for i in range(1, len(values)):
                value = values[i].strip()
                if(self.mapping.get(value) is None):
                    self.mapping[value] = index
                    self.mapping[index] = value
                    index += 1
                self.addEdges(self.mapping.get(name), self.mapping.get(value)) #populate matrix


    def getAllLanguages(self):
        s1 = set(self.vertices)
        s2 = set(self.interpreters)
        return s1-s2

    def printGraph(self):
        outputResultList = []
        outputResultList.append('--------Function printGraph--------')

        print('\t\t', end = '')
        for row in range(self.vertices):
            print(self.mapping.get(row), ' ', end ='')
        print()

        for row in range(self.vertices):
            print(self.mapping.get(row), ' ', end = '')
            for column in range(self.vertices):
                print(self.edges[row][column], '\t', end='')
            print()

        # for row in range(self.vertices):
        #     outputResultList.append(str(self.edges[row]))

        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def showAll(self):
        outputResultList = []
        outputResultList.append('--------Function showAll--------')
        outputResultList.append('Total no. of candidates: ' + str(len(self.interpreters)))
        outputResultList.append('Total no. of languages: '+ str(len(self.getAllLanguages())))
        outputResultList.append('\n')

        outputResultList.append('List of candidates:')
        for candidate in self.interpreters:
            outputResultList.append(candidate)

        outputResultList.append('\n')
        outputResultList.append('List of languages:')

        for language in self.getAllLanguages():
            outputResultList.append(language)

        outputResultList.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def displayCandidates(self, lang):
        outputResultList = []
        list = self.edges.get(lang)
        outputResultList.append('--------Function displayCandidates--------')
        outputResultList.append('List of Candidates who can speak '+ lang +':')
        for candidate in list:
            outputResultList.append(candidate)

        outputResultList.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def findDirectTranslator(self, langA, langB):
        outputResultList = []
        outputResultList.append('--------Function findDirectTranslator --------')
        outputResultList.append('LanguageA: '+ langA)
        outputResultList.append('LanguageB: ' + langB)
        candidates = self.edges.get(langA)
        #used dfs to iterate through langA and looking whether it is connected to the langB
        stack = []
        for candidate in candidates:
            stack.append(candidate)

        result = None
        while(len(stack)>0):
            item = stack.pop()
            langauges = self.edges.get(item)
            if(langB in langauges):
                result = item
                break

        if(result is None):
            outputResultList.append('Direct Translator: No. ')
        else:
            outputResultList.append('Direct Translator: Yes,'+ result+' can translate.')

        outputResultList.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def dfs(self, stack, visited, path, langB, prevPath):
        if(len(stack)>0):
            item = stack.pop()
            if (item not in visited):
                path.append(item)
                visited.append(item)
                vertices = self.edges.get(item)
                for vertex in vertices:
                    if(vertex not in visited):
                        stack.append(vertex)

                if (item == langB):
                    #need to check if we have found the shortest path
                    if(len(prevPath) >  0 and len(prevPath) > len(path)):
                        prevPath = path
                    else:
                        prevPath = path
                    visited.pop(visited.index(item))
                    # return True
            return self.dfs(stack, visited, path, langB, prevPath)
        else:
            if(len(path)>0 or len(prevPath)>0):
                return True
            return False

    def findTransRelation(self, langA, langB):
        outputResultList = []
        outputResultList.append('--------Function findTransRelation --------')
        outputResultList.append('LanguageA: '+ langA)
        outputResultList.append('LanguageB: ' + langB)

        #use dfs to iterate
        visited = [] #to keep track of which of the vertices
        stack = []
        path = [] # to track the path through vertices
        prevPath = [] #to track the last found path

        visited.append(langA)
        path.append(langA)
        connectedVertices = self.edges.get(langA)
        for vertices in connectedVertices:
            stack.append(vertices)

        found = self.dfs(stack, visited, path, langB, prevPath)
        pathString = None
        if(found):
            for val in path:
                if(pathString is None):
                    pathString = str(val)
                else:
                    pathString = pathString + '>'+ val
            outputResultList.append('Related: Yes, '+ pathString)
        else:
            outputResultList.append('Related: No, ')
        outputResultList.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(outputResultList)


    def displayHireList(self):
        #dfs , grraph greegy method prims or kruskal
        outputResultList = []
        outputResultList.append('--------Function displayHireList--------')

        langauges = list(self.getAllLanguages())
        allLanguageCovered = list(self.getAllLanguages())
        visited = [] #to track track of visited vertex
        hireList = [] #to keep count of interpreters
        stack = []

        startVertex = langauges[0]
        visited.append(startVertex)
        if(startVertex in langauges):
            allLanguageCovered.pop(allLanguageCovered.index(startVertex))
        for val in self.edges.get(startVertex):
            stack.append(val)

        while(len(stack)>0):
            item = stack.pop()
            if(item not in visited):
                visited.append(item)
                if (item not in langauges and item not in hireList):  # it's a candidate and not added to hirelist
                    if(self.hasAllLanguagesOfCurrentInterpreterAlreadyCovered(item, hireList)):
                        hireList.append(item)
                elif (item in langauges and item in allLanguageCovered): #remove if its langauage and has been covered
                    allLanguageCovered.pop(allLanguageCovered.index(item))
                vertices = self.edges.get(item)
                for vertex in vertices:
                    if(vertex not in visited):
                        stack.append(vertex)

            if(len(allLanguageCovered)<1):
                break

        outputResultList.append('No of candidates required to cover all languages: '+ str(len(hireList)))
        for hire in hireList:
            value = self.edges.get(hire)
            outputResultList.append(hire + ' / '+ ' / '.join(value))

        outputResultList.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(outputResultList)

    def hasAllLanguagesOfCurrentInterpreterAlreadyCovered(self, item, hireList):
        if(len(hireList) < 1):
            return True
        languages = self.edges.get(item)
        languagesCoveredSofar = []
        for interpreter in hireList:
            values = self.edges.get(interpreter)
            for val in values:
                languagesCoveredSofar.append(val)

        s1 = set(languages)
        s2 = set(languagesCoveredSofar)

        if(len(s1-s2)>0):
            return True
        else:
            return False
