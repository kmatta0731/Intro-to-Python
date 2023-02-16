# final.py

import sys
  
# this is good
def fibExpr(n):
    if n<=1:
        return '1'
    else:
        return f"({fibExpr(n-1)}+{fibExpr(n-2)})"


class CounterfeitError(Exception):
    pass
            
# based on list, can inherit for use composition    
class Wallet(list):

    denoms = [100,20,10,5,1]

    def __init__(self, bills=[]):
        self.addBills( bills)

    def __repr__(self):
        return f"Wallet({list.__repr__(self)})"

    def value(self):
        return sum(self)

    def add(self,bill):
        if bill in Wallet.denoms:
            self.append(bill)
        else:
            raise CounterfeitError(f"{bill} is a not a legal denomination!") 
        self.sort(reverse=True)

    def addBills(self,bills):
        for bill in bills:
            self.add(bill)

    def removeAmount(self,amount):

        for bill in Wallet.denoms:
            while bill in self and bill<=amount:
                self.remove(bill)
                amount -= bill
        return amount
            
        
from html.parser import HTMLParser

# class to collect title of document
class QuoteCollector(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.quotes = {}
        self.inQuote = False
    def handle_starttag(self,tag,attrs):
        if tag=='blockquote':
            self.inQuote = True
    def handle_data(self,data):
        if self.inQuote:
            quote,person = data.split('-')
            quote = quote.strip()
            person = person.strip()
            if person not in self.quotes:
                self.quotes[person] = [quote]
            else:
                self.quotes[person].append( quote )
    def handle_endtag(self, tag):
        if tag=='blockquote':
            self.inQuote = False
            
    def getQuotes(self):
        return self.quotes

   

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'finalTEST.py' ) )                


