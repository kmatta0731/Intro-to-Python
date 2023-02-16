# hw7TEST.py

>>> from hw7 import *


##### ImageCollector #####

>>> ic = ImageCollector( 'http://www.pmichaud.com/toast/' )
>>> ic.feed( urlopen('http://www.pmichaud.com/toast/').read().decode())
>>> type( ic.getImages() )
<class 'set'>
>>> sorted( ic.getImages() )
['http://www.pmichaud.com/toast/krnbo24.gif', 'http://www.pmichaud.com/toast/ptart-1c.gif', 'http://www.pmichaud.com/toast/toast-1b.gif', 'http://www.pmichaud.com/toast/toast-2c.gif', 'http://www.pmichaud.com/toast/toast-3c.gif', 'http://www.pmichaud.com/toast/toast-4c.gif', 'http://www.pmichaud.com/toast/toast-5c.gif', 'http://www.pmichaud.com/toast/toast-6c.gif']
>>> len( ic.getImages() )
8

##### ImageCrawler #####


>>> c = ImageCrawler()
>>> c.crawl('http://www.pmichaud.com/toast/',1,True)
>>> type( c.getImages() ) 
<class 'set'>
>>> sorted( c.getImages() )
['http://www.pmichaud.com/toast/krnbo24.gif', 'http://www.pmichaud.com/toast/ptart-1c.gif', 'http://www.pmichaud.com/toast/toast-1b.gif', 'http://www.pmichaud.com/toast/toast-2c.gif', 'http://www.pmichaud.com/toast/toast-3c.gif', 'http://www.pmichaud.com/toast/toast-4c.gif', 'http://www.pmichaud.com/toast/toast-5c.gif', 'http://www.pmichaud.com/toast/toast-6a.gif', 'http://www.pmichaud.com/toast/toast-6c.gif', 'http://www.pmichaud.com/toast/toast-7b.gif', 'http://www.pmichaud.com/toast/toast-8a.gif']
>>> len( c.getImages() )
11

##### scrapeImages #####

>>> scrapeImages('http://www.pmichaud.com/toast/','toast.html',1,True)
>>> open('toast.html').read().count('img')
11


