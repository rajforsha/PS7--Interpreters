from Utils import Utils
class Interpreter:

    def __init__(self, vertices):
        self.vertices = vertices # list containing languages and interpreter
        self.edges = [ [ None for i in range(vertices) ] for j in range(vertices) ] # adjency matrix of edges linking interpreters to languages
        self.interpreters = [] # need to maintain since vertices contain both the langauge and interpreter
        self.mapping = {} # mapping vertices to integer value
        self.utils = Utils()

    def addEdges(self, src, dest):
        # undirected graph, hence adding to both the ends
        self.edges[src][dest] = 1
        self.edges[dest][src] = 1

    def populateAdjacencyMatrixFromInputFile(self, filepath):
        data = self.utils.readFromInputFile(filepath)
        index = 0 # used for mapping
        for line in data:
            values = line.strip('\n').split('/')
            name = values[0].strip() # first word
            self.mapping[name]= index
            self.mapping[index] = name
            self.interpreters.append(name) # need to track interpreters
            index += 1
            for i in range(1, len(values)):
                value = values[i].strip()
                if(self.mapping.get(value) is None):
                    self.mapping[value] = index
                    self.mapping[index] = value
                    index += 1
                self.addEdges(self.mapping.get(name), self.mapping.get(value)) #populate matrix

    """def printGraph(self):
        output_result_list = []
        output_result_list.append('--------Function printGraph--------')

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
        #     output_result_list.append(str(self.edges[row]))

        # write to output file
        self.utils.writeToOutputFile(output_result_list)"""

    def getAllLanguages(self):
        languages = []
        # iterating through all the vertices and checking if the vertex is not an interpreter
        for row in range(self.vertices):
            if self.mapping[row] not in self.interpreters:
                languages.append(self.mapping[row])
        return languages

    def showAll(self):
        output_result_list = []
        output_result_list.append('--------Function showAll--------')
        output_result_list.append('Total no. of candidates: ' + str(len(self.interpreters)))
        output_result_list.append('Total no. of languages: '+ str(self.vertices - len(self.interpreters)))
        output_result_list.append('\n')

        output_result_list.append('List of candidates:')
        for candidate in self.interpreters:
            output_result_list.append(candidate)

        output_result_list.append('\n')
        output_result_list.append('List of languages:')

        for language in self.getAllLanguages():
            output_result_list.append(language)

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    def displayCandidates(self, lang):
        output_result_list = []
        list = [] #store all the candidate who can speak language queried for.
        index = self.mapping.get(lang)
        for row in range(self.vertices):
            if(self.edges[index][row] is not None):
                list.append(self.mapping.get(row))

        output_result_list.append('--------Function displayCandidates--------')
        output_result_list.append('List of Candidates who can speak '+ lang +':')
        for candidate in list:
            output_result_list.append(candidate)

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    def findDirectTranslator(self, langA, langB):
        output_result_list = []
        output_result_list.append('--------Function findDirectTranslator --------')
        output_result_list.append('LanguageA: '+ langA)
        output_result_list.append('LanguageB: ' + langB)

        stack = []
        result = None
        row = self.mapping.get(langA)
        for column in range(self.vertices):
            if(self.edges[row][column] is not None):
                stack.append(column)

        while len(stack)>0:
            item = stack.pop()
            # we need to just check whether the connected vertices has langB
            for col in range(self.vertices):
                if(self.edges[item][col] is not None and self.mapping.get(col) == langB):
                    result = self.mapping.get(item)
                    break

        if(result is None):
            output_result_list.append('Direct Translator: No. ')
        else:
            output_result_list.append('Direct Translator: Yes,'+ result+' can translate.')

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    def dfs(self, stack, visited, path, langB):
        if(len(stack)>0):
            item = stack.pop()
            if visited[item] is False:

                if (self.mapping.get(item) == langB):
                    return True # we have found the interpreters

                path.append(self.mapping.get(item)) # appending value from mapping
                visited[item] = True

                for col in range(self.vertices):
                    if visited[col] is False and self.edges[item][col] == 1:
                        stack.append(col)

            return self.dfs(stack, visited, path, langB)
        else:
            return False

    def findTransRelation(self, langA, langB):
        output_result_list = []
        output_result_list.append('--------Function findTransRelation --------')
        output_result_list.append('LanguageA: '+ langA)
        output_result_list.append('LanguageB: ' + langB)

        # use dfs to iterate
        visited = [False]*self.vertices # to keep track of which of the vertices
        stack = [] # dfs
        path = [] # to track the path through vertices
        stack.append(self.mapping.get(langA))

        found = self.dfs(stack, visited, path, langB)
        path_string = None
        if found:
            for val in path:
                if path_string is None:
                    path_string = str(val)
                else:
                    path_string = path_string + '>'+ val
            output_result_list.append('Related: Yes, '+ path_string)
        else:
            output_result_list.append('Related: No, ')
        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    def findMinimumInterpreters(self, stack, visited, languages, all_language_covered, hirelist):
        while(len(stack)>0):
            item = stack.pop()
            if(visited[item] is False):
                visited[item] = True
                for col in range(self.vertices):
                    if(self.edges[item][col] is not None):
                        if(self.mapping.get(col) in languages and self.mapping.get(col) in all_language_covered):
                            all_language_covered.pop(all_language_covered.index(self.mapping.get(col)))
                            if(self.mapping.get(item) not in hirelist):
                                hirelist.append(self.mapping.get(item))
                        else:
                            # its an interpreter
                            stack.append(col)
                if(len(all_language_covered)<1):
                    return
            else:
                self.findMinimumInterpreters(stack, visited, languages, all_language_covered, hirelist)

    def displayHireList(self):
        # dfs , graph greedy method prims or kruskal
        output_result_list = []
        output_result_list.append('--------Function displayHireList--------')

        languages = list(self.getAllLanguages())
        all_language_covered = list(self.getAllLanguages())
        visited = [False]*self.vertices # to track track of visited vertex
        hireList = [] # to keep count of interpreters
        stack = []

        for val in range(self.vertices):
            if(self.mapping.get(val) in self.interpreters and visited[val] is False):
                stack.append(val)
                self.findMinimumInterpreters(stack, visited, languages, all_language_covered, hireList)

        output_result_list.append('No of candidates required to cover all languages: ' + str(len(hireList)))
        for hire in hireList:
            language_known = []
            for col in range(self.vertices):
                if(self.edges[self.mapping.get(hire)][col] is not None):
                    language_known.append(self.mapping.get(col))
            output_result_list.append(hire + ' / ' + ' / '.join(language_known))

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

