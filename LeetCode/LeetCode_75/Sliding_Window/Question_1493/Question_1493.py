class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        arr = [ 0 ]

        prevZero = False
        addedZero = False

        for i in range( len( nums ) ) :

            if nums[ i ] :
                arr[ len( arr ) - 1 ] += 1

                if prevZero :
                    prevZero = False
                    addedZero = False
            else :
                if prevZero :
                    if addedZero : pass
                    else :
                        arr.append( 0 )
                        addedZero = True
                else :
                    arr.append( 0 )
                    prevZero = True
                    
        if len( arr ) == 1 : return arr[ 0 ] - 1

        maxVal = arr[ 0 ]

        for i in range( len( arr ) - 1 ) :
            maxVal = max( maxVal, arr[i] + arr[i+1])
         
        return maxVal
    
nums = [0,1,1,1,0,1,1,0,1]

print( f'longestSubarray : {Solution.longestSubarray( super, nums )}' )

# Beats 78.43% Runtime, 358ms
# Beats 61.22% Memory, 16.6mb