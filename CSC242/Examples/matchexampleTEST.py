#matchexampleTest.py
#you will be given this file!!

>>> from matchexample import *

>>> match('b?b', 'bob')
True
>>> match('b?b', 'boB')
False
>>> match('b?b', 'bb')
False

##>>> allMatches('bob', 'bob had apples bib bob bobby')
##['bob', 'bob']
##>>> allMatches('b?b', 'bob had apples bib bob bobby')
##['bob', 'bib', 'b b', 'bab', 'b b', 'bob']


          
