import random
# Take Max Size Int and Mod By Max
lenOfList = 100

# Return a List of random integers between zero and current maxInt
randomIntList = [ random.randint( 0, 100 ) for _ in range( lenOfList ) ]

target = 10
randomIntList.append( target )

def binarySearch( List, target) :
    
    min = 0
    max = len( List ) - 1
    guessIdx = round( max / 2 )
    
    while List[ guessIdx ] != target :     
        if( List[ guessIdx ] > target ) :
            max = guessIdx
            guessIdx = round( (max-min) / 2 ) + min
        else :
            min = guessIdx
            guessIdx = round( (max-min) / 2 ) + min
    
    print( 'Sorted List: ', List )
    print( 'Index Of Target Value: ', guessIdx )
      
# This removes duplicate values and sorts the list
# so you can get an accurate index of where the target is
randomIntList = list( set( randomIntList ) )
   
binarySearch( randomIntList, target )