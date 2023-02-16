# week8.py

# turtle graphics

# draw a square
'''
>>> draw('FLFLFLFL',100,90)
would draw same square
'''
from turtle import Screen, Turtle
def draw(directions, length=100, angle=90, x=0, y=0):
    ''' draw str directions, starting at x,y and then
    F - forward length
    L - left turn angle
    R - right turn angle
    '''
    # initialize
    s = Screen()
    t = Turtle()
    t.up() # dont draw on the way
    t.setpos(x,y)
    t.down()
    t.speed(100)

    # draw directions
    for move in directions:
        if move=='F':
            t.forward(length)
        elif move=='L':
            t.left(angle)
        elif move=='R':
            t.right(angle)
        else:
            print('this shouldnt happen')

    s.exitonclick()
        
'''
want this to work:
>>> koch(0) # base case
'F'
>>> koch(1)
'FLFRRFLF'
>>> koch(2)
FLFRRFLF L FLFRRFLF RR FLFRRFLF L FLFRRFLF
'''

def koch(n):

    if n==0: # base case
        return 'F'
    else:
        # much faster
        k = koch(n-1)        
        return k+'L'+k+'RR'+k+'L'+ k
        # much slower
        return koch(n-1)+'L'+koch(n-1)+'RR'+koch(n-1)+'L'+ koch(n-1)

# draw koch curve
#n = 5
#draw( koch(n), 400/3**n, 60, -200, 0)

# draw koch snowflake
n = 5
draw( 3*(koch(n)+'RR'), 400/3**n, 60, -200, 0)


    


