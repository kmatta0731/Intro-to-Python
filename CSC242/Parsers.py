# Parsers.py

##### HTMLParser #####

'''
We want to SCRAPE (extract) data from html
documents. To do this we will use:

HTMLParser - PARSES (breaks up) an html
document (a str) into start tags, end
tags, and data (in between).  When you
FEED the parser, it automatically calls
these methods as the items are
encountered.  Override these methods if
needed:

- handle_starttag
- handle_data
- handle_endtag

see also: BeautifulSoup

'''

##### PrintParser #####

from html.parser import HTMLParser

class PrintParser(HTMLParser):

    # three methods
    # parameters always the same
    def handle_starttag(self,tag,attrs):
        print( 'handle_starttag', tag, attrs)
    def handle_data(self,data):
        print( 'handle_data', data)
    def handle_endtag(self,tag):
        print( 'handle_data', tag )
              

'''
>>> p = PrintParser()
>>> p.feed( '<a target=blank href=https://www.cnn.com/>CNN</a>' )
handle_starttag a [('target', 'blank'), ('href', 'https://www.cnn.com/')]
handle_data CNN
handle_endtag a
>>> p.feed( open('sample.html').read() )
handle_starttag html []
handle_data 

handle_starttag head []
handle_data
'''

##### TitleCollector - collect data #####
'''
Suppose that we want to collect all titles
in the html document.  Note that a title
is encoded like this:

<title>Title - sample html document</title>

We want to collect DATA, the stuff
inbetween the tags.  But, we only want to
collect data that is in between start and
end title tags. To do this, will keep
track of whether or not we are currently
in a title. '''

class TitleCollector(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.titles = []
        self.inTitle = False
    def handle_starttag(self,tag,attrs):
        if tag == 'title':
            self.inTitle = True # turn collection on
    def handle_data(self,data):
        if self.inTitle==True:
            self.titles.append( data )
    def handle_endtag(self,tag):
        if tag == 'title':
            self.inTitle = False
    def getTitles(self):
        return self.titles
            
         
'''
>>> html = open('sample.html').read()
>>> tc = TitleCollector()
>>> tc.feed( html )
>>> tc.getTitles()
['Title - sample html document']
>>>
'''



    

    















                









