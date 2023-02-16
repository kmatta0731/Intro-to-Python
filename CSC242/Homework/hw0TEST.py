# hw0TEST.py

>>> from hw0 import *   # import code, file must be named hw1

##### hideShow #####

>>> hideShow( 'apple', '11001')
'ap##e'
>>> hideShow('apple','00000')
'#####'
>>> hideShow('apple','11111')
'apple'
>>> hideShow('abcdefghijklmnopqrstuvwxyz',13*'01')
'#b#d#f#h#j#l#n#p#r#t#v#x#z'
>>> hideShow( 'df###re##', '101010101' )
'd#####e##'
>>> 


>>> import random


##### moreOdds #####

>>> moreOdds( [2,3,4,5,7] )
True
>>> moreOdds( [2,3,4] )
False
>>> moreOdds( [2,3,4] ) == False
True
>>> moreOdds( [2,3,4,5] )
False
>>> moreOdds( [2,2,5,5] )
False
>>> random.seed(0)
>>> moreOdds( random.sample( range(100), 25) )
True
>>> random.seed(20)
>>> moreOdds( random.sample( range(100), 95) )
True
>>> random.seed(22)
>>> moreOdds( random.sample( range(100), 95) )
False
>>> 

##### flipSwitches #####


>>> flipSwitches( ['A','A','a','B'] )
{'B'}
>>> flipSwitches( 'ABCba')
{'C'}
>>> flipSwitches( 'sdfjSDSDFasjjfdjldsSDF' )=={'S', 'D', 'F'}
True
>>> random.seed(5)
>>> flipSwitches( [random.choice('abcdefABCDEF') for i in range(100)] )=={'D', 'B', 'F', 'C'}
True
>>> random.seed(100)
>>> flipSwitches( [random.choice('abcdefABCDEF') for i in range(10000)] )=={'D', 'E', 'A', 'F'}
True
>>> random.seed(0)
>>> flipSwitches( [random.choice('abcdefABCDEF') for i in range(10000)] )=={'E', 'A', 'C'}
True

##### numPairs #####

>>> numPairs( 3, [0,1,2,3] )
2
>>> numPairs( 4, [0,1,2,3] )
1
>>> numPairs( 6, [0,1,2,3] )
0
>>> numPairs( 4, [0,1,2,3,4,2] )
3
>>> numPairs( 4, [0,1,2,3,4,2,2] )
5
>>> numPairs( 4, [0,1,2,3,4,2] ) == 3  # print vs. return
True
>>> import random
>>> random.seed(0)
>>> numPairs( random.randrange(100), random.sample( range(100), 50 ) )
3
>>> random.seed(9)
>>> numPairs( random.randrange(100), random.sample( range(100), 50 ) )
13
>>> 

