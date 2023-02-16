# Kathie Mata
# hw2.py

class Pizza:
    def __init__(self, Size = 'M', Toppings = {}):
        self.top = set(Toppings)
        self.sze = Size
    def __repr__(self):
        return f"Pizza('{self.sze}',{self.top})"

    def setSize(self, Size):
        self.sze = Size

    def getSize(self):
        return self.sze

    def addTopping(self, topping):
        self.top.add(topping)
        
    def removeTopping(self, remove):
        self.top.remove(remove)

    def price(self):
        amntTop = len(self.top)
        if self.sze == 'S':
            return (.70 * amntTop) + 6.25
        if self.sze == 'M':
            return (1.45 * amntTop) + 9.95
        if self.sze == 'L':    
            return (1.85 * amntTop) + 12.95
            
    def __eq__(self, match):
        if self.top == match.top and self.sze == match.sze:
            return True
        else:
            return False

def orderPizza():
    print('Welcome to Python Pizza!')
    pSize = input('What size pizza would you like (S,M,L): ')
    pie = Pizza()
    pie.setSize(pSize)
    while True:
        pTopping = input('Type topping to add (or Enter to quit): ')
        if pTopping == '':
            break
        else:
            pie.addTopping(pTopping)
    print('Thanks for ordering!')
    print(f'Your pizza costs ${pie.price()}')
    return pie
    
         
   

