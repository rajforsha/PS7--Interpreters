# PS7--Interpreters-


#MainApplication.py
 - is the stating point of this assignment.
#Interpreter.py
 - is internally used by MainApplication.py
#Util.py 
- is the utility class to read/write to file.

#backup print method

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

Matrix:

		Manasa  English  Hindi  Punjabi  Venkat  Kannada  Tamil  Telugu  Paul  Malayalam  Marathi  Harish  Gujarati  Nisha  Bengali  Amjad  Parul  Rohan  Rahul  Sanjay  Surya  Zubin  
Manasa  None 	1 	1 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
English  1 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	1 	None 	1 	None 	1 	None 	None 	None 	1 	None 	1 	
Hindi  1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	1 	None 	1 	1 	None 	None 	None 	None 	1 	
Punjabi  1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	
Venkat  None 	1 	None 	None 	None 	1 	1 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Kannada  None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Tamil  None 	None 	None 	None 	1 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	1 	None 	
Telugu  None 	None 	None 	None 	1 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	
Paul  None 	None 	None 	None 	None 	None 	1 	1 	None 	1 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Malayalam  None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	1 	None 	
Marathi  None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	1 	None 	None 	None 	None 	1 	None 	None 	None 	
Harish  None 	1 	1 	1 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Gujarati  None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	
Nisha  None 	1 	1 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	
Bengali  None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	1 	None 	None 	
Amjad  None 	1 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Parul  None 	None 	1 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Rohan  None 	None 	None 	None 	None 	None 	1 	1 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Rahul  None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Sanjay  None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	
Surya  None 	None 	None 	None 	None 	None 	1 	None 	None 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
Zubin  None 	1 	1 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	None 	
   