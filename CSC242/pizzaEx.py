class Pizza:
    def __init__(self, addPizza = 'M', pizzaTopping = {}):
        self.x = addPizza
        self.y = set(pizzaTopping)
    def size(self, sizeOfPizza):
        self.x = sizeOfPizza
    def toppings(self, pizzaTopping):
       self.y = set(pizzaTopping)
    def __repr__(self):
        return("Pizza('{}',{})").format(self.x, self.y)
    def setSize(self,setSizePizza):
        self.x = setSizePizza
    def getSize(self):
        return self.x
    def addTopping(self, addPizzaTopping):
        self.y.add(addPizzaTopping)
    def removeTopping(self, removePizzaTopping):
        self.y.remove(removePizzaTopping)
    def price(self):
        amntTop = len(self.top)
        if self.sze == 'S':
            return (.70 * amntTop) + 6.25
        if self.sze == 'M':
            return (1.45 * amntTop) + 9.95
        if self.sze == 'L':    
            return (1.85 * amntTop) + 12.95
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


def orderPizza():
    pizza = Pizza()
    print("Welcome to Python Pizza!")
    addYourSize = input("What size pizza would you like (S,M,L): ")
    while True:
        addYourTopping = input("Type topping to add (or Enter to quit): ")
        if addYourTopping == '':
            break
        else:
            pizza.addTopping(addYourTopping)
        total = pizza.price()
    print("Thanks for ordering!")
    print("Your pizza costs $" + str(total))
    return pizza

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw2TEST.py'))
    
