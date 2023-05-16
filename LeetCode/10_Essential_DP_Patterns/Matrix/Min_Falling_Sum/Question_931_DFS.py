from functools import cache

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        rows = len( matrix )
        cols = len( matrix[ 0 ] )

        @cache
        def dynamic( row, col ) :

            if row == rows or col == cols or col < 0 :
                return float( 'inf' )
            
            elif row == rows-1 :
                return matrix[ row ][ col ]
            
            option1 = dynamic( row+1, col-1 )
            option2 = dynamic( row+1, col )
            option3 = dynamic( row+1, col+1 )
            
            return min( option1, option2, option3 ) + matrix[ row ][ col ]
        
        return min( [ dynamic( 0, col ) for col in range( cols ) ] )
    
matrix = [[2,1,3],[6,5,4],[7,8,9]]

print( f'Min Falling Sum: {Solution.minFallingPathSum( super, matrix )}' )

# Beats 31.99% Runtime, 159ms
# Beats 5.89% Memory, 25.2mb