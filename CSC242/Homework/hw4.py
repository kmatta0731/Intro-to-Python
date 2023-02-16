# hw4
# kathie Matta

class WordGame():

    def __init__(self, word = str().upper(), wrongGuess = str(), rightGuess = str()):
        self.word = word
        self.wrongGuess = wrongGuess
        self.rightGuess = rightGuess

    def __repr__(self):
        return f"({getState}, {getHint}, '{getRight}', '{getWrong}')"

    def getSecret(self):
        return self.word

    def guess(self, guess = str().upper()):
        if 'playing' not in self.getState():
            quit
        elif guess in self.rightGuess:
            quit
        elif guess in self.wrongGuess:
            quit
        elif guess in self.word:
            self.rightGuess += guess
        else:
            self.wrongGuess += guess

    def getHint(self):
        hidden = str()
        for letter in self.word:
            if letter in self.rightGuess:
                hidden += letter
            else:
                hidden += '?'
        return hidden

    def getRight(self):
        return self.rightGuess

    def getWrong(self):
        return self.wrongGuess

    def getState(self):
        if '?' not in self.getHint():
            return 'won'
        elif len(self.wrongGuess) > 5:
            return 'lost'
        else:
            return 'playing'


from tkinter import *
from tkinter.messagebox import showinfo
class WordGameGUI(Frame):

    def __init__(self,word = str(), parent=None):
        Frame.__init__(self,parent)
        self.wordgame = WordGame(word)
        
        #create Labels
        WordLabel = Label(self, text = 'Word:')
        WordLabel.grid(row = 0, column=0, columnspan=2)

        RightLabel = Label(self, text = 'Right:')
        RightLabel.grid(row=1, column=0, columnspan=2)

        WrongLabel = Label(self, text = 'Wrong:')
        WrongLabel.grid(row=2, column=0,columnspan=2)
        
        # Entries for the screen
        self.wordentry = Entry(self)
        self.wordentry.grid(row=0,column=1,columnspan=4)
        self.wordentry.insert(0,self.wordgame.getHint())

        self.rightentry = Entry(self)
        self.rightentry.grid(row=1, column=1, columnspan=4)
        #self.rightentry.insert(END,self.wordgame.getRight())

        self.wrongentry = Entry(self)
        self.wrongentry.grid(row=2, column=1, columnspan=4)
        #self.wrongentry.insert(END, self.wordgame.getWrong())

        # Buttons labels
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # create Buttons using a loop
        for i in range(len(letters)):
            # create customized function for each Button
            # local function (inside method)
            # could also use lambda/anonymous function
            def cmd(key=letters[i]):
                self.click(key)
            # create a button
            b = Button(self,command=cmd, text=letters[i],width=6,height=4)
            b.grid(row=i//6 + 3,column = i%6)

    # click event handler
    def click(self,key):
        self.wordgame.guess(key)
        self.wordentry.delete(0,END)
        self.wordentry.insert(0,self.wordgame.getHint())
        self.rightentry.delete(0,END)
        self.rightentry.insert(0, self.wordgame.getRight())
        self.wrongentry.delete(0,END)
        self.wrongentry.insert(0, self.wordgame.getWrong())
        if self.wordgame.getState() == 'won':
            showinfo('WordGame',str('You Win!'))
        elif self.wordgame.getState() == 'lost':
            showinfo('WordGame',str('You Lose!'))
        else:
            pass

if __name__ == '__main__':
    import doctest
    print(doctest.testfile('hw4TEST.py'))

