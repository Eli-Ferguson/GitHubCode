class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        n = len( matrix )

        for i in range( n-2, -1, -1 ) :

            for j in range( n ) :

                left = float( 'inf' ) if j == 0 else matrix[ i+1 ][ j-1 ]
                right = float( 'inf' ) if j == n-1 else matrix[ i+1 ][ j+1 ]
                down = matrix[ i+1 ][ j ]

                matrix[ i ][ j ] += min( left, right, down )
        
        return min( matrix[ 0 ] )

matrix = [[2,1,3],[6,5,4],[7,8,9]]

print( f'Min Falling Sum: {Solution.minFallingPathSum( super, matrix )}' )

# Beats 57.13% Runtime, 138ms
# Beats 15.75% Memory, 17.3mb