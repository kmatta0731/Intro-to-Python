# week9_2.py

'''
see:

HTML.py
sample.html
Parsers.py
'''

# read HTML documents using Python!

# on your local computer use open

# Parsers.py

# HTMLParser

##### PrintParser #####

from html.parser import HTMLParser

class PrintParser(HTMLParser):

    # three methods
    # parameters are always the same
    def handle_starttag(self,tag,attrs):
        print('handle_starttag',tag,attrs)
    def handle_data(self,data):
        print('handle_data', data )
    def handle_endtag(self,tag):
        print('handle_endtag', tag)

    
##### TitleCollector - collect data #####

''' we want to collect the data
inside the title tag

<title> Title - sample html document </title>

we want to collect data, the stuff in between tags
make a list of all titles found
'''

class TitleCollector(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        # make a bin to collect titles
        self.titles = []
        self.inTitle = False # are we inside a title tag

        # three methods
    # parameters are always the same
    def handle_starttag(self,tag,attrs):
        #print('handle_starttag',tag,attrs)
        if tag=='title':
            self.inTitle = True
    def handle_data(self,data):
        # print('handle_data', data )
        if self.inTitle == True:
        # or just: if self.inTitle:
            self.titles.append( data )
    def handle_endtag(self,tag):
        # print('handle_endtag', tag)
        if tag=='title':
            self.inTitle = False

    def getTitles(self):
        return self.titles















