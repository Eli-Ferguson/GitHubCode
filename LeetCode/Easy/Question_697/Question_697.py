class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        dict = {}

        for i in range( len( nums ) ) :

            if not nums[ i ] in dict :
                dict[ nums[ i ] ] = [ i, i, 1 ]
            else :
                arr = dict[ nums[ i ] ]
                
                dict[ nums[ i ] ] = [ arr[ 0 ], i, arr[ 2 ]+1 ]

        maxCount = 0
        start,end = 0,0
        for key, value in dict.items() :
            
            if value[ 2 ] == maxCount :
                if ( value[ 1 ] - value[ 0 ] ) < ( end - start ) :
                    start, end, maxCount = value[ 0 ], value[ 1 ], value[ 2 ]
                    
            if value[ 2 ] > maxCount :
                start, end, maxCount = value[ 0 ], value[ 1 ], value[ 2 ]

        return end-start+1

nums = [1,2,2,3,1,4,2]

print( f'Min Sub Arr With Degree: {Solution.findShortestSubArray( super, nums )}' )

# Beats 28.79% Runtime, 263ms
# Beats 5.18% Memory, 17.8mb