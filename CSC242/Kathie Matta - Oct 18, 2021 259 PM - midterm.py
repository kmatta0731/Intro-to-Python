#################### feedback ####################


MultipleChoice (out of 35) : 35

Heading (out of 30) : 27
 if self.d == match.d

TeamError  (out of 5) : 5

WinList (out of 30) : 20
WinList not WinLust - guess you werent able to doctest
init - must write, validate, change case
winPct, winnning - self, not self.inp, you are inheriting, right?  not using team argument


##################################################

#Kathie Matta
#Midterm

class Heading():
    directions = ['N', 'E', 'S', 'W']
    def __init__(self, direction = 'N'):
        self.d = direction

    def __repr__(self):
        return f"Heading('{self.d}')"

    def get(self):
        return self.d

    def right(self):
        newd = []
        try:
            for i in range(len(self.directions)):
                if self.d == self.directions[i]:
                    newd = self.directions[i+1]
            self.d = newd
        except IndexError:
            self.d = 'N'

    def left(self):
        newd = []
        try:
            for i in range(len(self.directions)):
                if self.d == self.directions[i]:
                    newd = self.directions[i-1]
            self.d = newd
        except IndexError:
            self.d = 'N'

    def __eq__(self, match):
        if self.match == self.d:
            return True
        else:
            return False
        
class TeamError(Exception):
    pass

class WinLust(list):
    def add(self, inp):
        self.inp = inp.upper()
        if self.inp != 'R' or self.inp != 'B':
            raise TeamError(f'{self.inp} is not a valid team')
        else:
            self.inp.append(inp)
    def __repr__(self):
        f"WinList({self.inp})"

    def winPct(self, team):
        if self.inp.count('R')> self.inp.count('B'):
            return self.inp.count('R')/ self.inp.count('B')
        if self.inp.count('B')> self.inp.count('R'):
            return self.inp.count('B')/ self.inp.count('R')

    def winning(self):
        if self.inp.count('R')> self.inp.count('B'):
            return 'R'
        if self.inp.count('B')> self.inp.count('R'):
            return 'B'
        else:
            return 'T'
if __name__ == '__main__':
    import doctest
    print(doctest.testfile('midtermTEST.py'))
    
    
        
    
