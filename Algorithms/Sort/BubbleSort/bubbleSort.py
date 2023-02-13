import sys, random
# Take Max Size Int and Mod By Max
maxInt = sys.maxsize % 999
lenOfList = 100

# Return a List of random integers between zero and current maxInt
randomIntList = [ random.randint( 0, maxInt ) for _ in range( lenOfList ) ]

def bubbleSort( List:list[int], ascending:bool ) :
    
    print( f'List Pre Sort:\n{List}')
    
    for n in range( len( List ) ) :
        for i in range( len( List ) - (n+1) ) :
            
            num1 = List[ i ]
            num2 = List[ i + 1 ]
                        
            if ( num1 > num2 and ascending ) or ( num1 < num2 and not ascending ):
                List[ i + 1 ] = num1
                List[ i ] = num2
        
    print( f'List Post Sort:\n{List}')
                        

# The list will be sorted according to the bool ascending
bubbleSort( randomIntList, ascending=True )