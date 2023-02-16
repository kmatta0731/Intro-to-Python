# LinkCollector.py

# extract/scrape/collect links from the
# href attribute in anchor tags <a>

##### links #####
'''
LINKS are connections (clickable text)
from one html document to another. They
are defined by the HREF ATTRIBUTE in the
ANCHOR TAG (<a>).

links found in html at:  https://www.cnn.com/

<a href="http://bleacherreport.com" ... >Sports</a>  
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
<a href="/world" ... >World</a>
   ^^^^^^^^^^^^^

The first is ABSOLUTE, the second
RELATIVE. But the relative link  "/world"
cannot be found without knowing it is
relative to https://www.cnn.com/.
'''

##### urljoin #####
'''
urljoin(base,url) - converts RELATIVE url
found at base into ABSOLUTE form.

>>> from urllib.parse import urljoin
>>> urljoin( 'http://cnn.com', '/world')
'http://cnn.com/world'
>>> # not just str addition
>>> urljoin( 'http://cnn.com', 'http://cnn.com/world')
'http://cnn.com/world'
>>> 
'''

##### LinkCollector #####
'''
Want to be able to scrape (collect) links
and store in SET(s)

want this to work:
>>> lc = LinkCollector('http://cnn.com') # base URL
>>> lc.feed( urlopen('http://cnn.com').read().decode() )
>>> lc.getAbsolutes()
... returns SET of absolute links ...
>>> lc.getRelatives()
... returns SET of relative links (written in absolute form)...
>>> lc.getLinks()
... returns SET of all links found ...
'''

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

class LinkCollector(HTMLParser):
    def __init__(self,url):
        HTMLParser.__init__(self)
        # add attributes
        self.url = url
        # sets  for storing links
        self.absolutes = set()
        self.relatives = set()

    def handle_starttag(self,tag,attrs):
        if tag=='a': # anchor
            # attrs is a list of tuples (pairs)
            #[('href', 'http://bleacherreport.com'), ('target', 'blank')]
            #print( attrs )
            for attr,val in attrs:
                if attr=='href':
                    # convert link to absolute form
                    link = urljoin(self.url,val)
                    if val[:4]=='http': # absolute
                        self.absolutes.add( link )
                    else: # relative
                        self.relatives.add( link )
                
        

    def getAbsolutes(self):
        return self.absolutes
    def getRelatives(self):
        return self.relatives
    def getLinks(self): # relative + absolute
        return self.absolutes.union( self.relatives )
        

##### scrapeLinks #####

# a LinkCollector client

'''
make this work:
>>> scrapeLinks( 'https://www.cnn.com/', 'cnn.html')
... scrapes all links at CNN and writes
them to an html document called cnn.html
...
'''

def scrapeLinks(url, filename):

    # use a LinkCollector to get links
    lc = LinkCollector(url)
    lc.feed( urlopen(url).read().decode() )

    # write the links to an html file
    with open(filename,'w') as file:

        file.write('<html><body>\n') # start html
        # write links
        for link in lc.getLinks():
            file.write( f"<a href={link}>{link}</a><br>\n" )
        # close html
        file.write('</body></html>') # end html
        
        

        















