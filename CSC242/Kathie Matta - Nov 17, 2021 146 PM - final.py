#################### feedback ####################

'''
multipleChoice (out of 25) : 20

fibWord (out of 25) : 25

CodeCollector (out of 25) : 25

MultiSet (out of 25) : 13
not really inheriting
add - parameter/attribute confusion
add - what is self.MS?   if self.items.count(addAmnt) < self.capacity then self.items.apped(addAmt)
init - add should be for single item not multiple items
eq - must compare actual items, use sorted()
'''
##################################################

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
        self.items = items
        self.capacity = capacity
    def __repr__(self):
        return f"MultiSet({self.capacity},{self.items})"
    def getCapacity(self):
        return self.capacity

    def add(self, addAmnt):
        if self.items.count(addAmnt) < self.capacity:
            self.items.append(addAmt)

    def remove(self, item):
        self.items.remove(item)
    def __eq__(self, match):
        if self.items.sorted() == match.items.sorted():
            return True
        else:
            return False
    
    
'''   
        
if __name__== '__main__':
    import doctest
    print( doctest.testfile('finalTest.py'))
   
'''
