class Stack():
    def __init__(self):
        self.item = list()

    def __repr__(self):
        return f"Stack({self.item})"
    

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        if len(self.item) == 0:
            return True
        else:
            return False
    def __getitem__(self, location):
        return self.item[location]

    def __len__(self):
        return len(self.item)

def parenthesesMatch(string):
    ''' given string, a sequence of ( and )'s returns True if they match, False
otherwise '''

    s = Stack()
    for char in string:
        #print(char)
        if char in '([{': 
            s.push(char)
        elif s.isEmpty():
            return False
        elif s.pop()+char not in ['()','[]','{}']:
            return False
        #print(s)
    return s.isEmpty()   

    
        
    
