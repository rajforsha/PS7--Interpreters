from Utils import Utils

class Census:

    def __init__(self):
        self.utils = Utils()
        self.birth_dist = {}
        self.death_dist = {}
        self.pop_dist = {}
        self.total_records = 0
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

        outputResultList = []
        outputResultList.append(str(self.total_records) + 'records captured.')
        # write to output file
        self.utils.writeToOutputFile(self.output_filepath, outputResultList)

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
        outputResultList = []
        outputResultList.append('No. of people born in' + str(year) + ':'+ str(dict.get(year)))
        # write to output file
        self.utils.writeToOutputFile(self.output_filepath, outputResultList)

    def countDied(self, dict, year):
        outputResultList = []
        outputResultList.append('No. of people died in' + str(year) + ':' + str(dict.get(year)))
        # write to output file
        self.utils.writeToOutputFile(self.output_filepath, outputResultList)


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
        else:
            print('invalid command')

