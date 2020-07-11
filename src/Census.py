from Utils import Utils
import sys

class Census:

    def __init__(self):
        self.utils = Utils()
        self.birth_dist = {}
        self.death_dist = {}
        self.pop_dist = {}
        self.total_records = 0
        self.outputResultList = []
        self.input_filepath = './inputPS3.txt'
        self.output_filepath = './outputPS3.txt'
        self.prompt_filePath = './promptsPS3.txt'

    def readInputData(self):
        lines = self.utils.readFromInputFile(self.input_filepath)
        for line in lines:
            data = line.strip('\n').split(',')
            dob = data[2]
            dod = None
            if len(data)>3:
                 dod = data[3]

            # extract year of birth and death
            birth_year = int(dob.split('-')[2])
            death_year = None
            if(dod is not None and len(dod)> 1):
                death_year = int(dod.split('-')[2])

            # we need to look for each map and update the value

            self.total_records += 1

            # update birth_dist and pop dis
            self.__updateMap(self.birth_dist, birth_year)
            self.__updateMap(self.pop_dist, birth_year)

            # update death_dist and pop list
            if death_year is not None:
                self.__updateMap(self.death_dist, death_year)
                self.__updateMap(self.pop_dist, death_year, '-')

        self.outputResultList.append(str(self.total_records) + 'records captured.')

    def __updateMap(self, dist, key, flag = '+'):

        # + we need to add, - we need to subtract

        if(dist.get(key) is not None):
            if flag == '+':
                dist[key] = dist.get(key) + 1
            else:
                dist[key] = dist.get(key) - 1
        else:
            if flag == '+':
                dist[key] = 1
            else:
                dist[key] = -1

    def countBorn(self, dict, year):
        self.outputResultList.append('No. of people born in' + str(year) + ':'+ str(dict.get(year)))

    def countDied(self, dict, year):
        self.outputResultList.append('No. of people died in' + str(year) + ':' + str(dict.get(year)))

    def maxPop(self, dict):
        year, max = self.__findMax(dict)
        self.outputResultList.append('Maximum population was in year ' + str(year)+ ' with ' + str(max)+ ' people alive.')

    def minPop(self, dict):
        year, min = self.__findMin(dict)
        self.outputResultList.append('Minimum population was in year ' + str(year) + ' with ' + str(min) + ' people alive.')

    def maxBirth(self, dict):
        year, max = self.__findMax(dict)
        self.outputResultList.append('Maximum births were in year ' + str(year) + ' with ' + str(max) + ' people born.')

    def maxDeath(self, dict):
        year, max = self.__findMax(dict)
        self.outputResultList.append('Maximum deaths were in year ' + str(year) + ' with ' + str(max) + ' people dead.')

    def printOutput(self):
        # write to output file
        self.utils.writeToOutputFile(self.output_filepath, self.outputResultList)

    def __findMax(self, dict):
        return self.__findMinMax(dict, '+')

    def __findMin(self, dict):
        return self.__findMinMax(dict, '-')


    def __findMinMax(self, dict, flag):
        # + for max and - for min
        year = None
        value = sys.maxsize if flag == '-' else -sys.maxsize
        for k, v in dict.items():
            if flag == '+':
                if (v > value):
                    value = v
                    year = k
            else:
                if (v > value):
                    value = v
                    year = k

        return year, value

if __name__ == '__main__':
    ob = Census()
    ob.readInputData()
    # now we need to read the command to output value
    command_list = ob.utils.readFromInputFile(ob.prompt_filePath)
    for command in command_list:
        if 'bornIn' in command:
            values = command.split(':')
            ob.countBorn(ob.birth_dist, values[1])
        elif 'diedIn' in command:
            values = command.split(':')
            ob.countBorn(ob.death_dist, values[1])
        elif 'maxPopulation' in command:
            ob.maxPop(ob.pop_dist)
        elif 'minPopulation' in command:
            ob.minPop(ob.pop_dist)
        elif 'maxBirth' in command:
            ob.maxBirth(ob.birth_dist)
        elif 'maxDeath' in command:
            ob.maxDeath(ob.death_dist)
        else:
            print('invalid command')

    # finally we write the output to file
    ob.printOutput()
