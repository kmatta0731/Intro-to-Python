# Kathie Matta
#collab w chris flores
#hw3.py

class Stat(list):
    def __repr__(self):
        return f"Stat({list.__repr__(self)})"
    
    def add(self, number):
        list.append(self, number)

    def min(self):
        if len(self) > 0:
            return min(self)
        else:
            raise EmptyStatError('empty Stat does not have a min')

    def max(self):
        if len(self) > 0:
            return max(self)
        else:
            raise EmptyStatError('empty Stat does not have a max')

    def sum(self):
        return sum(self)
        
    def mean(self):
        if len(self) > 0:
            return sum(self)/len(self)
        else:
            raise EmptyStatError('empty Stat does not have a mean')

class EmptyStatError(Exception):
    pass

class intlist(list):
    def insert(self, index, item):
        if type(item)==int:
            list.insert(self, index, item)
        else:
            raise NotIntError(f"{item} not an int")
    def __setitem__(self, index, item):
        if type(item) == int:
            list.__setitem__(self, index, item)
        else:
            raise NotIntError(f"{item} not an int")
    def append(self, item):
        self.insert(len(self), item)

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def odds(self):
        odds = intlist()
        for i in intlist(self):
            if i % 2 == 1:
                odds.append(i)
        return odds

    def evens(self):
        evens = intlist()
        for i in self:
            if i % 2 == 0:
                evens.append(i)
        return evens
            

    def __init__(self, iterable = []):
        self.extend(iterable)

    def __repr__(self):
        return f"intlist({list.__repr__(self)})"
    

class NotIntError(Exception):
    pass

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw3TEST.py'))
       

