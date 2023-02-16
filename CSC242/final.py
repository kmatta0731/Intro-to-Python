#final
# Kathie Matta

def fibWord(n):
    if n == 0:
        return '0'
    else:
        x,y = '01', '0'
        for i in range(2,n+1):
            x,y = x+y, x
        return x

from html.parser import HTMLParser
class CodeCollector(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.codes = []
        self.inCode = False
    def handle_starttag(self,tag, attrs):
        if tag == 'code':
            self.inCode = True
    def handle_data(self, data):
        if self.inCode:
            self.codes.append(data)
    def handle_endtag(self, tag):
        if tag == 'code':
            self.inCode = False
    def getCode(self):
        return self.codes

class MultiSet(list):
    MS = []
    def __init__(self, capacity, items = [] ):
        self.add(items)
        self.capacity = capacity
        
    def __repr__(self):
        return f"MultiSet({self.capacity},{self.MS})"
    def getCapacity(self):
        return self.capacity
    def add(self, items):
        for i in items:
            if self.MS.count(i) < self.capacity:
                self.MS.append(i)
        return self.MS 

    def remove(self, item):
        self.items.remove(item)
    def __eq__(self, match):
        if self.items == match.items:
            return True
        else:
            return False
    
    

    
'''       
if __name__== '__main__':
    import doctest
    print( doctest.testfile('finalTest.py'))
'''
