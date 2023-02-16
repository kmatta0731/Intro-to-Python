# hw5.py
# Kathie Matta

def levy(n):
    if n == 0:
        return 'F'
    else:
        l= levy(n-1)
        return 'L' + l + 'RR' + l + 'L'

def fibWord(n):
    if n == 0:
        return '0'
    else:
        x, y = '01', '0'
        for i in range(2, n+1):
            x, y = x + y, x
        return x
       
def nested(n):
    if n == 1:
        return [1]
    else:
        return [nested(n-1)] + [[1]]

def printCollatz(n):
    print(n, '', end='')
    if n == 1:
        quit
    elif n % 2 == 0:
        return printCollatz(n//2)
    elif n % 2 == 1:
        return printCollatz(3*n + 1)

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5.py') )
