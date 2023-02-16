# lab2.py
# Kathie Matta
# collab: Tepmontree Rattanawit

class Animal:
    def __init__ (self, Species = 'default', Language = 'default', Age = 0):
        self.spec = Species
        self.lang = Language
        self.age = Age

    def setSpecies(self, Species):
        self.spec = Species

    def setLanguage(self, Language):
        self.lang = Language

    def setAge(self, Age):
        self.age = (Age)

    def speak(self):
        print(f'I am a {self.age} year-old {self.spec} and I {self.lang}.')

    def __repr__(self):
        return f"Animal('{self.spec}','{self.lang}',{self.age})"


def processAnimals(file):
    infile = open(file, 'r')
    txt = infile.readlines()
    infile.close()
    animalList = []

    for i in txt:
        print(i)
        splittext = i.split(',')
        species, language, age = splittext[0], splittext[1], int(splittext[2])
        animalList.append(Animal(species, language, age))
        print(animalList)
##    for a in animalList:
##        a.speak()
##    return animalList
##    
##
##if __name__=='__main__':
##    import doctest
##    print( doctest.testfile('lab2TEST.py') )

