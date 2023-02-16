# Kathie Matta
# lab1.py
# collabs: Alex N.
# 09/14/2021
'''
def printTwoLargest():
    num = []
    number = eval(input('Please enter a number: '))
    while number > 0:
        num.append(number)
        number = eval(input('Please enter a number: '))
    num.sort()
    num.reverse()
    if len(num) == 1:
        print('The largest is', num[0])
    elif len(num) > 1:
        print('The largest is', num[0])
        print('The second largest is', num[1])
    else:
        print('No positive numbers were entered')

 '''   

def printWordsLines():
    if input == 'test1.txt':
        infilelines = open('CSC242\CSC242_Lab1\test1.txt','r')
        text = infilelines.readlines()
        lines = len(text)
        infilelines.close()
        infilewords = open('CSC242\CSC242_Lab1\test1.txt','r')
        text = infilewords.read()
        text = text.split()
        words = len(text)
        infile.close()
    elif input == 'test2.txt':
        infilelines = open('CSC242\CSC242_Lab1\test2.txt','r')
        text = infilelines.readlines()
        lines = len(text)
        infilelines.close()
        infilewords = open('CSC242\CSC242_Lab1\test2.txt','r')
        text = infilewords.read()
        text = text.split()
        words = len(text)
        infile.close()
    print('The file', input, 'contains', words,'words and', lines, 'lines')

    
'''


def reverseDict(dictionary):
    x = {value:key for key, value in dictionary.items()}
    return(x)
        
    #instructor solution
    newdict = {}
    for key in dictionary: # value is d[key]
        #put the reverse in the newdict
        #d[key] = value
        value = dictionary[key] #old key and value
        newdict[value=] = key
    return newdict
    



if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab1TEST.py' ))
'''

