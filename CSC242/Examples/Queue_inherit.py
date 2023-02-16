# Queue_inherit.py

##### CuttingError #####
'''
CuttingError is a custom exception.
raised when setitem is called

q[1]=11 # raises CuttingError
'''
class CuttingError(Exception):
    pass

##### Queue - v2 - inheritance #####

# mantra: self IS A list instance
# self DOES NOT have an attribute .q
# DO NOT say self.q

# DO NOT MIX inheritance and composition

class Queue(list):

    # __init__ is inherited
    # already does what we want
    # try not writing __init__!

    # EXTENDED method
    def __repr__(self):
        return f"Queue({list.__repr__(self)})"
        return "Queue({})".format(list.__repr__(self))

    # ADDED methods
    def enqueue(self,item):
        self.append(item)
    def dequeue(self):
        return self.pop(0)
    
    # q[1] = 'Sally' -> Queue.__setitem__(q,1,'Sally')
    def __setitem__(self,index,item):
        raise CuttingError('no cutting, you bad code!')        
    
    # inherit:
    # __getitem__,__eq__, __len__

    # EXTEND
    def __add__(self,other):
        return Queue( list.__add__(self,other) )
        # dont do this - CIRCULAR
        # return Queue( self+other )

    

##### NOTE: circular definitions #####

'''
Be CAREFUL about CIRCULAR definitions
that will cause INFINITE RECURSION.

class Queue(list):

    def __repr__(self):        
        return f"Queue({self))"
        return "Queue({})".format(self)

To execute either return statement:
- self must be converted to a str
- this calls __repr__!
- which __repr__?
- self is a Queue
- this calls Queue.__repr__!
- method calls itself
- circular definition/infinite recursion
- produces:

"Queue(Queue(Queue(Queue(Queue(...))))"
'''
##### try/except with CuttingError #####

'''
>>> q = Queue(range(5))
>>> q
Queue([0, 1, 2, 3, 4])
>>> try:
	q[1]=99
except CuttingError:
	print('hey no cutting!')

	
hey no cutting!
>>>
'''


##### doctest #####

# NOTE: change import to Queue_inherit

if __name__=='__main__':
    import doctest
    print( doctest.testfile('queuesTEST.py'))
    
      







        
        
    

    
