#coding = utf-8

class NormWords(object):

    def __init__(self):
        self.filePath = 'alice.txt'

    def read_file(self, file):
        try:
            with open(file) as file_object:
                contents = file_object.read()
        except FileNotFoundError:
            print("File Not Found!")
        else:
            return contents

    def count_words(self, contents, word):
        explicite_number = contents.count(word)
        norm_number = contents.lower().count(word)
        
        print("The File contains words " + word + " as many as " + str(explicite_number))
        print("The File contains words(Upper or Lower Cases's ingnored) " + word + " as much as " + str(norm_number))


counter = NormWords()
contents = counter.read_file(counter.filePath)
counter.count_words(contents, 'alice')
        
