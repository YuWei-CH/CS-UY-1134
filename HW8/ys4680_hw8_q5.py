from ChainingHashTableMap import ChainingHashTableMap
import string
class InvertedFile:
    def __init__(self, file_name):
        file = open(file_name, "r")
        read_file = file.read()
        read_file = read_file.translate( read_file.maketrans( '','', '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' ) )
        str = read_file.split()

        self.map = ChainingHashTableMap()

        for i in range(len(str)):
            str[i] = str[i].lower()
            try:
                self.map[str[i]]
            except KeyError:
                self.map[str[i]] = []
                self.map[str[i]].append(i)
            else:
                self.map[str[i]].append( i )
        file.close()

    def indices(self, word):
        try:
            return self.map[word]
        except KeyError:
            return []
'''
inv_file = InvertedFile('row your boat.txt')
print(inv_file.indices("row"))
print(inv_file.indices("the"))
print(inv_file.indices("done"))
'''