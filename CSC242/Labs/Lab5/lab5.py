#lab5.py
#kathie Matta w/ Alex

class Temperature():
    def __init__(self, temp = float(), unit = 'c'):
        if type(temp) == float or int:
            self.t = float(temp)
        else:
            raise ValueError(f"Could not convert string to float: '{temp}'")
        if unit == 'c' or unit == 'C' or unit == 'f' or unit == 'F':
           self.u = unit.upper() 
        else:
            raise UnitError(f"Unrecognized temperature unit '{unit}'")
    def __repr__(self):
        return f"Temperature({self.t},'{self.u}')"     
        
    def convert(self):
        if self.u == 'C':
            faren = (self.t * 9/5) + 32
            return Temperature(faren, 'F')
        elif self.u == 'F':
            cel = (self.t - 32) * 5/9
            return Temperature(cel, 'C')
        
    def __str__(self):
        return f"{self.t}°{self.u}"
    
    def __eq__(self, match):
        if self.u == match.u:
            if self.t == match.t:
                return True
            else:
                return False
        else:
            if self == match.convert():
                return True
            else:
                return False
            
class valueError(Exception):
    pass

class UnitError(Exception):
    pass

#from Temperature import *
from tkinter import *
from tkinter.messagebox import showinfo

class TempConverter(Frame):
    
    
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        #Create Temperature Label
        templabel = Label(self, text = 'Temperature:')
        templabel.grid(row = 0, column = 0, columnspan = 2)

        #Create Unit label
        unitlabel = Label(self, text = 'Unit(C or F):')
        unitlabel.grid(row = 1, column = 0, columnspan = 2)

        #Create Temp Entry
        self.TempEntry = Entry(self)
        self.TempEntry.grid(row=0, column=2, columnspan=3)
        
        #Create Unit Entry
        self.UnitEntry = Entry(self)
        self.UnitEntry.grid(row = 1, column = 2, columnspan = 3)

        #Create Button
        b = Button(self, command = self.doConvert, text = 'Click to Convert')
        b.grid(row = 2, column = 2)
        
        
    def doConvert(self):
        try:
            # retrieve text from unit entry
            temp = self.TempEntry.get()
            # retrieve text from temp entry
            unit = self.UnitEntry.get()
            t1 = Temperature(temp, unit)
            t2 = Temperature(temp,unit)
            #pop-up conversion box
            showinfo('Conversion', str(t1)+" = "+str(t2.convert()))
        except UnitError:
            showinfo('Error:', str('Unit should be either C or F'))
        except ValueError:
            showinfo('Error:', str('Temperature must be decimal or integer'))

  
  
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab5TEST.py'))
      
        
        
    
    
        
