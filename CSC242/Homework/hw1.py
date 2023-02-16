# hw1.py
# Kathie Matta

class Volume:
    def __init__ (sound, Default = 0):
        sound.vol = Default
        sound.set(sound.vol)
    def set(sound, amount):
        if amount < 0:
            sound.vol = 0
        elif amount > 11:
            sound.vol = 11
        else:
            sound.vol = amount
            
    def __repr__(sound):
        return f"Volume({sound.vol})"
    
    def get(sound):
        return (sound.vol)
    
    def up(sound, IncreaseAmnt):
        sound.vol += (IncreaseAmnt)
        sound.set(sound.vol)
        
    def down(sound, DecreaseAmnt):
        sound.vol = sound.vol - (DecreaseAmnt)
        sound.set(sound.vol)
        
    def __eq__(sound, match):
        return sound.vol == match.vol

def partyVolume(file):
    
    infile = open(file, 'r')
    line = eval(infile.readline())
    
    v = Volume()
    v.set(line)
    txt = infile.readlines()
    
    for i in txt:
        splittext = i.split()
        if splittext[0] == 'U':
            v.up(eval(splittext[1]))
        if splittext[0] == 'D':
            v.down(eval(splittext[1]))         
    return v
      
    infile.close()  
        

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw1TEST.py'))    
        
    
        


    
