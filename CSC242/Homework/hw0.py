# hw0.py
# Kathie Matta

def hideShow(s, masking):
    InputString = ''
    for i in range(len(masking)):
        masksplit = masking[i]
        if masksplit == '0':
            InputString += '#'
        else:
            InputString += s[i]
    return InputString


def moreOdds(Integers):
    odds = []
    evens = []
    for i in range(len(Integers)):
        if Integers[i] % 2 == 1:
            #Help from 'codefather.tech' for %2 to find odds
            odds.append(Integers[i])
        else:
            evens.append(Integers[i])
    if len(odds) > len(evens):
        return True
    else:
        return False
    

def flipSwitches(switches):
    switch = set()
    for i in range(len(switches)):
        switch.add(switches[i])
        Off = switches[i].lower()
        if Off == switches[i]:
            switch.discard(switches[i])
            switch.discard(switches[i].upper())
    return switch

def numPairs(target, s):
    pairs = []
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] + s[j] == target:
                pairs.append(target)
    return len(pairs)

    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw0TEST.py'))

