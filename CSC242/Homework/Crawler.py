# Crawler.py

##### Crawler #####
'''
A Crawler object will recursively CRAWL
web pages, i.e., read html and follow
links to other web pages, which will then
be crawled ...

Methods:

crawl(url, depth, relativeOnly) - starting
at url, recursively crawl web pages up to
depth.  relativeOnly - follow relative
links only.

getCrawled() - return set of urls whose
html was READ

getFound() - return set of urls/links that
were FOUND (includes crawled, but also
ones of greater depth)

getDead() - return set of urls/links that
could NOT succesfully be READ
'''

from urllib.error import *
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

# put LinkCollector.py in same folder
from LinkCollector import LinkCollector

class Crawler: # does not inherit
    def __init__(self): # create "bins" for collection
        self.crawled = set() # urls that have been read
        self.found = set() # urls that are found, but not neccesarily read
        self.dead = set() # urls that could not be read
    def getCrawled(self):
        return self.crawled
    def getFound(self):
        return self.found
    def getDead(self):
        return self.dead

    # c.crawl( 'https://www.cnn.com/', depth=2, relativeOnly = True)
    def crawl(self,url,depth, relativeOnly=True):
        # read the html at url
        # and collect links found there
        lc = LinkCollector(url)
        try:
            html = urlopen(url).read().decode()
            lc.feed( html )
        except (UnicodeDecodeError, HTTPError, URLError, TypeError):
            self.dead.add( url )
        self.crawled.add( url ) # we just read it!
        # extract links, depends on relativeOnly
        if relativeOnly: # == True
            links = lc.getRelatives()
        else:
            links = lc.getLinks()
        self.found.update( links )
        # recursively crawl the links that we found
        if depth>0:
            for link in links:
                if link not in self.crawled:  # not a tree
                    self.crawl(link,depth-1, relativeOnly)

'''

>>> c = Crawler()
>>> c.crawl( 'https://www.cnn.com/', depth=2, relativeOnly = True)
... takes a little while ...
>>> len( c.getCrawled() )
157
>>> len( c.getFound() )
4353
>>> len( c.getDead() )
2
>>> c.getDead()
{'https://www.cnn.com/newsletters', 'https://www.cnn.com/email/subscription'}
>>> list( c.getCrawled() )[:10]
['https://www.cnn.com/travel/food-and-drink', 'https://www.cnn.com/collection', 'https://www.cnn.com/videos/weather/2018/10/10/hurricane-michael-hits-florida-panhandle-orig-tc.cnn', 'https://www.cnn.com/videos/weather/2019/09/03/climate-change-global-warming-what-can-i-do-chad-myers-nws-orig.cnn', 'https://www.cnn.com/videos/weather/2016/08/29/orig-weather-preparing-for-a-hurricane.cnn', 'https://www.cnn.com/travel/videos/travel/2020/05/05/chef-pati-jinich-three-ingredients-recipes-orig-jm.cnn', 'https://www.cnn.com/travel/article/national-beer-day-2020/index.html', 'https://www.cnn.com/travel/videos', 'https://www.cnn.com/videos/weather/2020/05/21/weather-tropical-cyclone-amphan-updates-intl-hnk-vpx.cnn', 'https://www.cnn.com/specials/weather/weather-video']
>>> list( c.getFound() )[:10]
['https://www.cnn.com/videos/us/2018/06/12/fl-toll-booth-car-crash-orig-vstan-bdk.cnn', 'https://www.cnn.com/2020/05/21/cnn-underscored/memorial-day-appliance-sales/index.html', 'https://www.cnn.com/2015/01/02/world/sponsorships-policy/index.html', 'https://www.cnn.com/style/article/artsy-smiley-face-origin/index.html', 'https://www.cnn.com/election/2020/state/puerto-rico', 'https://www.cnn.com/2019/05/28/opinions/mueller-congress-testimony-campbell/index.html', 'https://www.cnn.com/profiles/nick-watt', 'https://www.cnn.com/2018/10/29/cnn-underscored/moosejaw-rewards-shop/index.html', 'https://www.cnn.com/videos/business/2020/05/15/fresh-money-blade-and-blue-peter-papas-orig-jg.cnn-business/video/playlists/stories-worth-watching/', 'https://www.cnn.com/2018/05/21/us/mike-pompeo-fast-facts/index.html']


>>> urlopen('https://www.cnn.com/newsletters')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
...
raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden
'''

