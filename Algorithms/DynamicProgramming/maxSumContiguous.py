arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSum( arr ) :
    
    dp = [ min( arr ) for _ in arr ]
    print( dp )
    
    # d[ i ] will represent the max sum of an array up to d[ i ]
    
    dp[ 0 ] = arr[ 0 ]
    
    for i in range( 1, len( arr ) ) :
        
        if dp[ i-1 ] > 0 : # If previous is positive add to current arr value
            dp[ i ] = dp[ i-1 ] + arr[ i ]
        else : # if previous is negative keep only the current arr value
            dp[ i ] = arr[ i ]
    
    print( dp )
    return max( dp )

print( maxSum( arr ) )