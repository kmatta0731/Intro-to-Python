# Kathie Matta
# hw6.py

def pascalLine(n):
    if n == 0:
        return [1]
    else:
        answer = [1]
        prevLine = pascalLine(n-1)
        for i in range(len(prevLine)-1):
            Sum = prevLine[i]+prevLine[i+1]
            answer.append(Sum)
        answer.append(1)
    return answer
            
def base(n, b):
    if n<b:
        return str(n)
    else:
        return base(n//b,b) + base(n%b,b)

def iPattern(n,k=0):
    if n== 1:
        print(k*' '+"\\")
    else:
        iPattern(n//3,k)
        for i in range(n//3):
            print((k+n//3)*' '+n//3*'0')
        iPattern(n//3,k+2*n//3)

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw6TEST.py') )
