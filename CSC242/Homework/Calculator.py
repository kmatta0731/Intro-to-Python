# Calculator.py
'''
Calculator laid out on 6X4 grid:

     0   1   2   3
   +---------------+
 0 |    SCREEN     | <- Entry
   +---+---+---+---+
 1 | 0 | 1 | 2 | 3 |
   +---+---+---+---+
 2 | 4 | 5 | 6 | 7 |
   +---+---+---+---+   
 3 | 8 | 9 | + | - | <- Buttons
   +---+---+---+---+
 4 | * | / | ( | ) |
   +---+---+---+---+
 5 | . | % | = | C | <- = computes
   +---+---+---+---+    C(lear)

Buttons create by loop, labels given by:

labels = "0123456789+-*/().%=C"

GRID buttons, placement depends on index.
"(" has index 14, grid at:
row = 4 col = 2

      0    1   2    3
   +-------------------+
 0 |       SCREEN      |
   +----+----+----+----+
 1 | 0  | 1  | 2  | 3  |
   +----+----+----+----+
 2 | 4  | 5  | 6  | 7  |
   +----+----+----+----+
 3 | 8  | 9  | 10 | 11 | <- indices of 
   +----+----+----+----+    buttons
 4 | 12 | 13 | 14 | 15 |
   +----+----+----+----+
 5 | 16 | 17 | 18 | 19 |
   +----+----+----+----+
   


"(" has index 14, position is:
col = 2 = 14%4
row = 4 = 14//4 + 1,   

NOTE: +1 for screen which occupies 1 row.

GRID button with index i at:
col = 14%4
row = i//4 + 1

tables from:
https://www.tablesgenerator.com/text_tables#
'''


##### Calculator #####

# model for hw: WordGameGUI

from tkinter import *
class Calculator(Frame):

    def __init__(self,parent=None):
        # always do this
        Frame.__init__(self,parent)
        
        # Entry for the screen
        self.entry = Entry(self, font=("Courier 20"))
        self.entry.grid(row=0,column=0,columnspan=4)        

        # Buttons labels
        labels = "0123456789+-*/().%=C"
        # create Buttons using a loop
        for i in range(len(labels)):
            # create customized function for each Button
            # local function (inside method)
            # could also use lambda/anonymous function
            def cmd(key=labels[i]):
                self.click(key)
            # create a button
            b = Button(self,command=cmd, text=labels[i],width=7,height=3,font=("Courier 12"))
            b.grid(row=i//4 + 1,column = i%4)

    # click event handler
    def click(self,key):
        # print( 'click', key )
        if key=='=':
            # calculate
            # get data - contents of entry
            expr = self.entry.get()
            # perform calculation
            try:
                ans = eval(expr)
            except:
                ans = 'ERROR'
            # output results
            self.entry.delete(0,END)
            self.entry.insert(END,ans)
            
        elif key=='C':
            # clear
            self.entry.delete(0,END)
        else: # other button
            # write key into entry
            self.entry.insert(END,key)


# Calculator().pack()











