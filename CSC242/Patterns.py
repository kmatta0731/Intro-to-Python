# kathie matta
# lab7
# i work by myself


def silly(n):
    if n > 0:
        print('*', end = '')
        silly(n-1)
        print('!', end = '')

def stars(n):
    if n > 0:
        stars(n-1)
        print(n * '*')
        stars(n-1)

def pattern(n):
    if n== 1:
        print(n, end ='')
    else:
        pattern(n//2)
        
        print(n, end='')
        

if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab7TEST.py') )
        
        
        
        
        
