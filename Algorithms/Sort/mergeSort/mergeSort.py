import random
lenOfList = 100

randomIntList = [ random.randint( 0, 1000 ) for _ in range( lenOfList ) ]

def merge( List1:list, List2:list ) :
    
    l1p = 0
    l2p = 0
    
    ret = []
            
    while ( len(List1) ) != l1p and ( len(List2) ) != l2p :
        if List1[l1p] < List2[l2p] :
            ret.append( List1[l1p] )
            l1p+=1
        else :
            ret.append( List2[l2p] )
            l2p+=1
                        
    if l1p != len( List1 ) : ret += List1[l1p:]
    if l2p != len( List2 ) : ret += List2[l2p:]
        
    return ret

def mergeSplit( List:list ) :
    
    if len( List ) == 1 : return List
    
    low = 0
    high = len( List )
    mid = round( ( high-low ) / 2 )
    
    bottomHalf = mergeSplit( List[low:mid] )
    topHalf = mergeSplit( List[mid:high] )
        
    return merge( bottomHalf, topHalf )

print( 'List Pre Sort: ', randomIntList )
print( 'List Post Sort: ', mergeSplit( randomIntList ) )