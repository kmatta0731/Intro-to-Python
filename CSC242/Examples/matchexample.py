
def match(pattern,s):
    #different lengths- not match
    if len(pattern) != len(s):
        return False
    #iteration loop#
    for i in range(len(pattern)):
        #if mismatch return true/false
        if pattern[i] != '?' and pattern[i] != s[i]:
           # print(i, pattern[i], s[i])
            return False
    return True


def allMatches(pattern,s):
    # accumulaate a list of matches
    matches = [] #initialize 
    for i in range(len(s)):
        # if a match print
        if match(pattern,s[i:i+len(pattern)]):
            matches.append( s[i: i+len(pattern)]) #accumulate/collect  
            #print(i, s[i:i+len(pattern)])
    return matches
        
#doctest snippet - add to the bottom of code

if __name__ == '__main__':
    import doctest
    print( doctest.testfile('matchexampleTEST.py'))

