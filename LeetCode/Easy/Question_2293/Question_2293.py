class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

        if len( nums ) == 1 : return nums[ 0 ]

        operation = 1

        while len( nums ) != 1 :

            tmp = [ 0 ] * int( len(nums) / 2 )

            for i in range( 0, len( nums ), 2 ) :

                if operation :
                    tmp[ int( i / 2 ) ] = min( nums[ i ], nums[ i +  1] )
                    operation = 0
                else :
                    tmp[ int( i / 2 ) ] = max( nums[ i ], nums[ i +  1] )
                    operation = 1
                        
            nums = tmp
        
        return nums[ 0 ]

nums = [1,3,5,2,4,8,2,2]
print( f'Min Max Alternate: {Solution.minMaxGame( super, nums )}' )

# Beats 93.26% Runtime, 51ms
# Beats 98.7% Memory, 13.9mb