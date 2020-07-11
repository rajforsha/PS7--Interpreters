from Utils import Utils
import sys
"""
this is the class which has implementation for all the methods required for this assignment
private methods:
__addEdges
__getAllLanguages
__bfs
__findMinimumInterpreters
public methods:
readApplications
showAll
displayCandidates
findDirectTranslator
findTransRelation
displayHireList
"""

class Interpreter:

    """
    this is the __init__ method
    vertices: this contains the total number of vertex of graph
    edges : this is the adjacency matrix created, the matrix is m[vertices][vertices] size: vertices*vertices
    interpreters: this is the list we need to maintain as vertex can be either language or interpreter
    mapping: since the input is string(vertex), we create mapping for the vertex
            example harish -> 1 h[1]= harish, h[harish]=1
            this is created for each vertex
    utils: we need this class to write to file and read from file
    """
    def __init__(self, vertices):
        self.vertices = vertices # total number of vertices
        self.graph = [[None for i in range(vertices)] for j in range(vertices)] # adjency matrix of edges linking interpreters to languages
        self.interpreters = [] # need to maintain since vertices contain both the langauge and interpreter
        self.mapping = {} # mapping vertices to integer value
        self.utils = Utils()

    # since the graph is undirected, for each src and dest, we create the mapping.
    def __addEdges(self, src, dest):
        # undirected graph, hence adding to both the ends
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1

    """
    we populate the matrix here.
    filepath : path to the input file
    we start with index-0, since we need to create the mapping, so that graph iteration would be easy. starting row 0- row n
    we also create the interpreter list, as we need to distinguish between language and interpreter
    so while reading the input file, we know the first word is interpreter and rest is languages
        example: Manasa /English / Hindi / Punjabi
                Manasa is interpreter
                english, hindi and punjabi are labguages
    we create the mapping for each vertex as well and finally
         example harish -> 1 h[1]= harish, h[harish]=1
                this is created for each vertex
    we create the adjacency matrix by calling __addEdges method
    """
    def readApplications(self, filepath):
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
                self.__addEdges(self.mapping.get(name), self.mapping.get(value)) #populate matrix

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
                print(self.graph[row][column], '\t', end='')
            print()

        # for row in range(self.vertices):
        #     output_result_list.append(str(self.edges[row]))

        # write to output file
        self.utils.writeToOutputFile(output_result_list)"""

    """
    since we have the list of interpreters, now its easy to distinguish, hence we iterate for all the vertices
    and whichever item is not in interpreter, we know its a language
    """
    def __getAllLanguages(self):
        languages = []
        # iterating through all the vertices and checking if the vertex is not an interpreter
        for row in range(self.vertices):
            if self.mapping[row] not in self.interpreters:
                languages.append(self.mapping[row])
        return languages

    """
    this method displays the list of languages and interpreters
    as we already have the list of languages and interpreters
    languages: __getAllLanguages
    interpreters: self.interpreters
    """
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

        for language in self.__getAllLanguages():
            output_result_list.append(language)

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    """
    lang: given a language, we need to find all the candidate who can speak particualr language
    since we already have the matrix, its very now, we just need to iterate for all the column for that particular row
    and print everything for which the m[row][col] is not None
    """
    def displayCandidates(self, lang):
        output_result_list = []
        list = [] #store all the candidate who can speak language queried for.
        row = self.mapping.get(lang)
        for col in range(self.vertices):
            if(self.graph[row][col] is not None):
                list.append(self.mapping.get(col))

        output_result_list.append('--------Function displayCandidates--------')
        output_result_list.append('List of Candidates who can speak '+ lang +':')
        for candidate in list:
            output_result_list.append(candidate)

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    """
    langA: language A given
    langB: language B given
    for langA we need to find all the cols for which the value is not None and put it into the stack
    then we iterate through the stack and for each value, we look into all the columns and check if the value is
    not None and it is equal to langB
    if we get the link, we store it to result.
    """
    def findDirectTranslator(self, langA, langB):
        output_result_list = []
        output_result_list.append('--------Function findDirectTranslator --------')
        output_result_list.append('LanguageA: '+ langA)
        output_result_list.append('LanguageB: ' + langB)

        stack = []
        result = None
        row = self.mapping.get(langA)
        for column in range(self.vertices):
            if(self.graph[row][column] is not None):
                stack.append(column)

        while len(stack)>0:
            item = stack.pop()
            # we need to just check whether the connected vertices has langB
            for col in range(self.vertices):
                if(self.graph[item][col] is not None and self.mapping.get(col) == langB):
                    result = self.mapping.get(item)
                    break

        if(result is None):
            output_result_list.append('Direct Translator: No. ')
        else:
            output_result_list.append('Direct Translator: Yes,'+ result+' can translate.')

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    """
    private Method
    this is the modified version of bfs, which we have used to find the minimum distance between the
    2 vertex
    src: langA
    dest: langB
    we main 2 list pred: it contains the parent name
    dist: this list contains the actual distance from src to all the vertices
    we make use of visited, so that we don't visit the same vertex again.
    return: True-> we have a link
            False-> no link between src and dest
    """
    def __bfs(self, pred, dist, langA, langB):
        queue = []
        visited = [False]*self.vertices
        for i  in range(self.vertices):
            visited[i] = False
            pred[i] = -1
            dist[i] = sys.maxsize

        visited[self.mapping.get(langA)] = True;
        dist[self.mapping.get(langA)] = 0
        queue.append(self.mapping.get(langA))

        while(len(queue)>0):
            item = queue.pop(0)
            for col in range(self.vertices):
                if(self.graph[item][col] is not None and visited[col] is False):
                    visited[col] = True
                    dist[col] = dist[item] + 1
                    pred[col] = item
                    queue.append(col)

                    if(self.mapping.get(col) == langB):
                        return True
        return False

    """
    it takes 2 paramter langA and langB and returns the relation between them.
    we make use of private method bfs.
    """
    def findTransRelation(self, langA, langB):
        output_result_list = []
        output_result_list.append('--------Function findTransRelation --------')
        output_result_list.append('LanguageA: '+ langA)
        output_result_list.append('LanguageB: ' + langB)

        pred = [0] * self.vertices
        dist = [0] * self.vertices

        if (self.__bfs(pred, dist, langA, langB) is False):
            output_result_list.append('Related: No, ')
        else:
            path = []
            crawl = self.mapping.get(langB)

            path.append(self.mapping.get(crawl))
            while(pred[crawl]!= -1):
                path.append(self.mapping.get(pred[crawl]))
                crawl = pred[crawl]

            path_string = None
            while(len(path)>0):
                val = path.pop()
                if path_string is None:
                    path_string = str(val)
                else:
                    path_string = path_string + '>'+ val

            output_result_list.append('Related: Yes, '+ path_string)

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)

    """
    this is a private method
    we use dfs to iterate over the matrix 
    stack: store the vertex to be visited
    visited: keep track so that we don't visit the same vertex again
    languages: actual language list, we need as the vertex can be either interpreter as well as language
    all_language_covered: initially it has all the languages, once we visit a language, we remove from this list
    all_language_covered: if the list is empty, we have the interpreters who can cover all the languages
    for each language, we remove. we add it to the hirelist and we don't add the same interpreter again if it is there
    in the hirelist.s
    """
    def __findMinimumInterpreters(self, stack, visited, languages, all_language_covered, hirelist):
        while(len(stack)>0):
            item = stack.pop()
            if(visited[item] is False):
                visited[item] = True
                for col in range(self.vertices):
                    if(self.graph[item][col] is not None):
                        if(self.mapping.get(col) in languages and self.mapping.get(col) in all_language_covered):
                            all_language_covered.pop(all_language_covered.index(self.mapping.get(col)))
                            if(self.mapping.get(item) not in hirelist):
                                hirelist.append(self.mapping.get(item))
                        else:
                            # it's an interpreter
                            stack.append(col)
                if(len(all_language_covered)<1):
                    return
            else:
                self.__findMinimumInterpreters(stack, visited, languages, all_language_covered, hirelist)

    """
    This method takes care of getting the minimal hirelist those can cover all the languages.
    it internally calls __findMinimumInterpreters and get all the hirelist
    once we get the hirelist, we iterate for item for all the cols and if the value is not None
    we populate it to list
    """
    def displayHireList(self):
        # dfs
        output_result_list = []
        output_result_list.append('--------Function displayHireList--------')

        languages = list(self.__getAllLanguages())
        all_language_covered = list(self.__getAllLanguages())
        visited = [False]*self.vertices # to track track of visited vertex
        hireList = [] # to keep count of interpreters
        stack = []

        for val in range(self.vertices):
            if(self.mapping.get(val) in self.interpreters and visited[val] is False):
                stack.append(val)
                self.__findMinimumInterpreters(stack, visited, languages, all_language_covered, hireList)

        output_result_list.append('No of candidates required to cover all languages: ' + str(len(hireList)))
        for hire in hireList:
            language_known = []
            for col in range(self.vertices):
                if(self.graph[self.mapping.get(hire)][col] is not None):
                    language_known.append(self.mapping.get(col))
            output_result_list.append(hire + ' / ' + ' / '.join(language_known))

        output_result_list.append('-----------------------------------------')
        # write to output file
        self.utils.writeToOutputFile(output_result_list)
