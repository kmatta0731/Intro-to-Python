>>> from midterm import *

##### Heading #####
   
>>> # construct with argument
>>> h = Heading('E')
>>> h
Heading('E')
>>> # without argument
>>> h = Heading()
>>> h
Heading('N')
>>> h.get()
'N'

>>> # right, not all checked here
>>> h = Heading()
>>> h
Heading('N')
>>> h.right()
>>> h
Heading('E')
>>> h.right()
>>> h
Heading('S')
>>> h.right()
>>> h
Heading('W')
>>> # left, not all checked here
>>> h = Heading('E')
>>> h.left()
>>> h
Heading('N')
>>> h.left()
>>> h
Heading('W')

>>> Heading('E')==Heading('E')
True
>>> Heading('W')==Heading('S')
False
>>> h = Heading() # 'N'
>>> h.right()
>>> h == Heading('E')
True

##### TeamError #####

>>> raise TeamError() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TeamError
>>> raise TeamError('your message here') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TeamError: your message here


##### WinList #####

>>> w = WinList()
>>> w.add('R')
>>> w
WinList(['R'])
>>> w.add('R')
>>> w.add('B')
>>> w.add('b')
>>> w.add('r')
>>> w
WinList(['R', 'R', 'B', 'B', 'R'])
>>> w = WinList()
>>> w.add('q') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TeamError: q is not a valid team
>>> w.add(3) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TeamError: 3 is not a valid team

>>> w = WinList( ['R','b','B','R'] )
>>> w
WinList(['R', 'B', 'B', 'R'])
>>> w = WinList( ['R','q','B','R'] ) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TeamError: q is not a valid team
>>> w = WinList( [3,'B','R'] ) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
TeamError: 3 is not a valid team

>>> w = WinList( ['R','b','B','R','r','r'] )
>>> w = WinList( ['R','B','B','B'] )
>>> w.winPct('B')
0.75
>>> w.winPct('R')
0.25
>>> w = WinList( ['R','b','B','R','r','r'] )
>>> w.winPct('R')
0.6666666666666666
>>> w.winPct('B')
0.3333333333333333

>>> w = WinList( ['R','b','B','R','r','r'] )
>>> w.winning()
'R'
>>> w = WinList(['B','R'])
>>> w.winning()
'T'
>>> w = WinList( ['R','b','B','R','r','r','B','B','B'] )
>>> w.winning()
'B'
