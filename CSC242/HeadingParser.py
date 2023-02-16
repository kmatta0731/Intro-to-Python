# Kathie Matta
# lab9.py
# I work alone

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

class HeadingParser(HTMLParser):
          def __init__(self):
                    HTMLParser.__init__(self)
                    self.headings = []
                    self.inheadings = False
          def handle_starttag(self,tag,attrs):
                    if tag in [ 'h1', 'h2', 'h3']:
                              self.inheadings = True

          def handle_data(self, data):
                    if self.inheadings:
                              self.headings.append(data.strip())
                    for item in self.headings:
                              if item == '':
                                        self.headings.remove(item)

          def handle_endtag(self, tag):
                    if tag in [ 'h1', 'h2', 'h3']:
                              self.inheadings = False

          def getHeadings(self):
                    return self.headings

def testHP(url=str()):
          hp = HeadingParser()
          html = urlopen(url).read().decode()
          hp.feed( html )
          return hp.getHeadings()




if __name__=='__main__':
      import doctest
      
      print( doctest.testfile('lab9TEST.py'))    


     
        
