from ChainingHashTableMap import ChainingHashTableMap
import re

class InvertedFile:
    file=""
    
    def __init__(self,file_name):
        f = open(file_name,"r")
        self.dictionary = ChainingHashTableMap()
        lines = f.readlines()
        i = 0
        for line in lines:
            words = re.split(' ', line)
            for word in words:
                if word == ' ' or word == '' or word == '\t' or word == '\n':
                    pass
                else:
                    santized_word = self.sanitize(word)
                    if santized_word not in self.dictionary:
                        self.dictionary[santized_word] = []
                    self.dictionary[santized_word].append(i)
                    i += 1
  
    def indices(self,word):
        santized_word = self.sanitize(word)
        if santized_word not in self.dictionary:
            return []
        return self.dictionary[santized_word]

    def sanitize(self, word):
        result = []
        for char in word:
            lower_char = char.lower()
            if lower_char.isalpha():
                result.append(lower_char)
        return ''.join(result)
            
    
inv_file=InvertedFile('C:\\Users\\alexz\\Desktop\\CS1134\\HW9\\testfile.txt')