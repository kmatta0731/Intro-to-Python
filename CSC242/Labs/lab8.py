#lab8.py
#kathie Matta
# I work by myself

def printPattern(n, k=0):
    if n== 1:
        print(k*' '+'*')
    else:
        
        printPattern(n//2,k)
        print(k*' ' + n*'*')
        printPattern(n//2,n//2+k)

def gcd(m,n):
    if n == 0:
        return m
    elif m == 0:
        return n
    elif m >= n:
        return gcd(n, m-n)
    elif n>=m:
        return gcd(m, n-m)
        
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = f(n-2)
        y = f(n-1)
        for i in range(n):
            return float((x+y)/2)

if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab8TEST.py') )
