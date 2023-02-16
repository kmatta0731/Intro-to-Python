# Kathie Matta
# lab4.py
# Collabs: Alex N, Jessenia

class Counter(dict):

    def __repr__(self):
        return f"Counter({dict.__repr__(self)})"


    def count(self, number):
        if number not in self.keys():
            self[number] = 0
        if number in self.keys():
            self[number] += 1
            
    def __getitem__(self, index):
        if index in self:
            return dict.__getitem__(self,index)
        else:
            return 0

    def countItems(self, inputlist):
        for i in inputlist:
            self.count(i)

    def printCounts(self):
        for i in sorted(self):
            print(i,self[i])
        

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab4TEST.py'))    
            
    


    
        
