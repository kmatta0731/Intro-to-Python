# KochCurve.py

# (math) fun!

##### turtle graphics #####

# turtle graphics - you DO NOT need to
# know turtle graphics you only need to
# worry about the "code"

'''
this draws a square

>>> from turtle import Screen,Turtle
>>> s = Screen()
>>> t = Turtle()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>>

also:
t.setpos(x,y)
t.up() - pen up, dont draw
t.down() - pen down, draw
'''

# slightly different from text
from turtle import Screen, Turtle
def draw( directions, length=100, angle=90, x=0,y=0):
    ''' draw str directions, starting at x,y
        and then
        F - forward by length
        L - left turn angle
        R - right turn angle
    '''
    # initialize
    s = Screen()
    t = Turtle()
    t.up()
    t.setpos(x,y)
    t.down()
    t.speed(100)

    # draw directions
    for move in directions:
        if move=='F':
            t.forward(length)
        elif move=='R':
            t.right(angle)
        elif move=='L':
            t.left(angle)
        else:
            print( 'bad move' )

    s.exitonclick()

# to draw a square
# draw('FLFLFLFL',100,90)

# draw triangle
# draw(3*'FLL',100,60)

##### koch curve/snowflake #####

'''
want this to work (angles = 60 degrees)

>>> koch(0) # base case
'F'
>>> koch(1)
'FLFRRFLF'
>>> koch(2)
'FLFRRFLF' + 'L' + 'FLFRRFLF' + 'RR' + 
'FLFRRFLF' + 'L' + 'FLFRRFLF'

>>> koch(n) # recursive case
koch(n-1) + 'L' + koch(n-1) + 'RR' +
koch(n-1) + 'L' + koch(n-1)
'''

def koch(n):
    if n==0: # base case
        return 'F'
    else: # recursive case
        k = koch(n-1)
        return k + 'L' + k + 'RR' + k + 'L' + k
        # above more efficient than
        return koch(n-1) + 'L' + koch(n-1) \
               + 'RR' + koch(n-1) + 'L' + koch(n-1)

# draw koch curve
#n = 4
#draw( koch(n), 400/3**n, 60, -200, 0)

# Koch snowflake
n = 4
draw( 3*(koch(n)+'RR'), 400/3**n, 60, -200, 0)


##### Fractals ######
'''

Koch curve is a an example of a FRACTAL.
For more on fractals, start at wikipedia:
https://en.wikipedia.org/wiki/Fractal.

And, for a very cool fractal video, check
out:

https://www.youtube.com/watch?v=fMwrWsDcSKE
'''








