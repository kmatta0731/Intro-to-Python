# HTML.py

'''
Last topic: use Python to scrape (collect
data) and crawl web pages.
'''

##### HTML crash course #####

# see sample.html for example
'''
HTML - hypertext markup language

An HTML document is a TEXT document with
its content "marked up" to for rendering
(display) in a web browser (Chrome,
Firefox, ...)


some TAGS:

html - stuff inside is html
head - header, title etc.
body - what you see displayed on main page
h1,h2,...h6 - headers
p - paragraph
br - (line) break, no closing tag
a - anchor, e.g. LINK
img - image
ol - ordererd list
ul - unordered list
li - list item
 

TAG ANATOMY:

    <a target=blank href=https://www.cnn.com/> CNN </a>

- start tag - <a>
- data - "CNN" - the stuff between open and closing tags (displayed)
- attribute/value - href=https://www.cnn.com/
- end tag - </a>
- can be multiple attribute/value pairs in
  an opening tag (and in any order)
- not all tags have closing tags


URLs - Universal Resource Locator
       e..g., address

ABSOLUTE url - resource can be located
without knowing location of html document

    img - https://ichef.bbci.co.uk/wwfeatures/live/976_549/images/live/p0/7k/4h/p07k4hnq.jpg
    link - https://www.cnn.com/

RELATIVE url - resource can only be found
by its location relative to the html
document

    img - shark.jpg - in same folder 
    link - doc.html - in same folder

'''

##### read HTML documents using Python #####

'''
HTML documents are text documents.
Access them (obtain str) as follows:

open/read - open and read html file on
your computer
    
in urllib.request

urlopen/read/decode - open, read and
decode html file on remote server

urlretrieve - use to download files to
your computer


READING HTML FILES:

local file:

>>> open('sample.html').read()[:100]
'<html>\n<head>\n<title>Title - sample html document</title>\n</head>\n<body>\n<h1>Sample html document</h'
>>>

remote, use urllib.request:

>>> # remote file
>>> from urllib.request import *
>>> html = urlopen("https://www.cnn.com/").read().decode()
>>> html[:100]
'<!DOCTYPE html><html class="no-js"><head><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatibl'
>>> html.count('</a>')
228
>>> html.count('img')
146
>>> # we wont use this, but it is super useful
>>> urlretrieve('https://ichef.bbci.co.uk/wwfeatures/live/976_549/images/live/p0/7k/4h/p07k4hnq.jpg','shark2.jpg')
('shark2.jpg', <http.client.HTTPMessage object at 0x048BD6F0>)
>>>
'''

