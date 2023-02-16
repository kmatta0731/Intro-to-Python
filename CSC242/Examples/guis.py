# guis.py

##### GUIs/tkinter #####
'''
GUI
- graphical user interface
- POINT and CLICK interface using mouse,
  touchscreen (vs TEXT based interface)

API
- application programming interface
- LIBRARY of class/functions/methods
  that allow you to manipulate objects
  in some environment

tkinter
- a Python GUI API
- lots of prebuilt WIDGETS
- also can CREATE our own WIDGETS using
  inheritance
'''
##### tkinter widgets #####
'''
Tk()
- main (root) window
- cannot be parented to soemthing else

Frame
- container for other widgets
- subclass Frame to build custom widget

Label
- display text
- text="whatever"
- user cant change directly

Entry
- user editable textbox
- Entry is the object, not
  the text itself
- .get() will return text
- .insert(END,txt) - appends text
- .delete(0,END) - deletes all text

Button
- text='click me'
- command=eventHandler
  Runs the function/method eventHandler
  when the button is clicked.  must be
  callable WITHOUT arguments.

showinfo
- dialog

choose ONE method for layout:

pack()
- adds widget to the bottom of a column

grid(row=i,column=j,rowspan=rspan,
columnspan=cspan)

- place widget in GRID
- top-left of grid is row,col = (0,0)
- top-left of widget is (i,j)
- widget SPANS rspan rows, cspan columns
  (default to 1)
'''

##### tkinter/widgets #####
'''
>>> from tkinter import Tk, Label
>>> root = Tk()
>>> hello = Label(root,text='hello,world!')
>>> hello.pack()
>>> 
>>> 
>>> # greedy import
>>> from tkinter import *
>>> Button(root, text='click me').pack()
>>> 
>>> # create an Entry - for user text
>>> # always names an Entry!
>>> e = Entry()
>>> e.pack()
>>> e
<tkinter.Entry object .!entry>
>>> # to access text, use get()
>>> e.get()
'type stuff in entry'
>>> 
>>> # note that this doesnt work well
>>> e2 = Entry().pack()
>>> e2.get()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    e2.get()
AttributeError: 'NoneType' object has no attribute 'get'
>>> # create a function
>>> # function must be callable
>>> # without arguments
>>> def f():
	print( 'hi!' )

	
>>> Button(root,text='say hi!',command=f).pack()
>>> hi!
hi!
hi!
hi!
hi!
hi!
hi!
hi!
hi!
hi!
hi!
KeyboardInterrupt
>>> def f():
	print( 'hi!' + e.get() )

	
>>> Button(root,text='say hi!',command=f).pack()
>>> hi!fred
hi!fred
hi!fred
hi!fred
hi!fred

'''




















