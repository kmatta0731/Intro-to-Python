# Kathie Matta
#hw7

from LinkCollector import LinkCollector  
from Crawler import Crawler
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import URLError


class ImageCollector(HTMLParser):

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.imgs = set()# is set correct?
        self.url = url

    def handle_starttag(self, tag, attrs):
        if tag == 'img':# is img correct?
            for attr,val in attrs:
                if attr == 'src': # is onclick correct?
                    #collect the value
                    #strip out "audioplay('" and "')"
                   link = urljoin(self.url, val)
                   self.imgs.add(link)
    def getImages(self):
        return self.imgs

class ImageCrawler(Crawler):

    def __init__(self):
        Crawler.__init__(self)
        self.imgs = set()
        
    def Crawl(self, url, depth, relativeOnly = True):
        #before crawling, gather img's from url
        collector = ImageCollector(url)
        try:
            collector.feed(urlopen(url).read().decode())
        except:
            print('Error reading url')
##            pass
        self.imgs.update( collector.getImages())
        Crawler.crawl(self, url, depth, relativeOnly)

    def getImages(self):
        return self.imgs

def scrapeImages(url, filename, depth, relativeOnly=True):
    #crawl! not collect
    ic = ImageCrawler()
    ic.crawl(url, depth, relativeOnly=True)

    #write the mp3s to html file filename
    with open(filename,'w') as f:
        f.write('<html><body>\n')
        for image in ic.getImages():
            f.write( f"{image}<img src='{images}'></img>\n")
        f.write('</body></html>')

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw7TEST.py') )

                
