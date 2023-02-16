# lab3
# Kathie Matta

class Stack:
    def __init__ (self):
        self.i = []
    def __repr__(self):
        return f'Stack({self.i})'

    def push(self, item):
        self.i.append(item)
        

    def pop(self):
        return self.i.pop()

    def isEmpty(self):
        if len(self.i) == 0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.i)

    def __getitem__(self, location):
        return self.i[location]

def parenthesesMatch(characters):
    s = Stack()
    for y in characters:
        if y == '(' '[' '{':
            s.push(y)
            if y == ')':
                s.pop('(')
            elif y == '}':
                s.pop('{')
            elif y == ']':
                s.pop('[')
            else:
                return False
            if len(s) == 0 and y == ')' '}' ']':
                return False
       
            if len(s) == 0:
                return True
                print('true')
        
            
        
    


##    return True
##    else:
##        return False
##            
##    
##    

