import random
# Take Max Size Int and Mod By Max
lenOfList = 100

# Return a List of random integers between zero and current maxInt
randomIntList = [ random.randint( 0, 100 ) for _ in range( lenOfList ) ]


target = 10

def linearSearch( List, target) :
    
    if len( [ val for val in range( len(List) ) if List[ val ] == target ] ) : print( f'{target} is in list:\n {List}' )
    else : return print( f'{target} is not in list:\n {List}' )

linearSearch( randomIntList, target )