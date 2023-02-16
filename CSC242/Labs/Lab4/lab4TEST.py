# lab4TEST.py

>>> from lab4 import *



##### Counter #####

>>> c = Counter()
>>> c.count( 1 )
>>> c.count( 1 )
>>> c.count( 3 )
>>> c.count( 5 )
>>> c
Counter({1: 2, 3: 1, 5: 1})

>>> c[1]
2
>>> c[5]
1
>>> c[99]
0

>>> c = Counter()
>>> c.countItems( [3,1,2,1,3,2,3] )
>>> c
Counter({3: 3, 1: 2, 2: 2})

>>> c.printCounts()
1 2
2 2
3 3

make sure that class is really inheriting:

>>> c = Counter()
>>> c.count(5)
>>> isinstance(c,dict) # inheriting?
True
>>> len(vars(c))==0  # inheriting?
True


more thorough tests:

>>> from random import *
>>> seed(0)
>>> c = Counter()
>>> c.countItems( [randrange(5) for i in range(5)])
>>> c
Counter({3: 2, 0: 1, 2: 1, 4: 1})
>>> c.printCounts()
0 1
2 1
3 2
4 1
>>> c.countItems( [randrange(5) for i in range(500)])
>>> c.printCounts()
0 115
1 93
2 99
3 97
4 101
>>> 
