class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:

        mx = 0
        for i in range( len( matrix ) ) :

            for j in range( len( matrix[ 0 ] ) ) :

                if matrix[ i ][ j ] == '0' :
                    matrix[ i ][ j ] = 0
                else:
                    if i == 0 or j == 0 :
                        matrix[ i ][ j ] = 1
                    else :
                        matrix[ i ][ j ] = min(
                            matrix[ i-1 ][ j-1 ], # prev diagonal
                            matrix[ i-1 ][ j ], # prev above
                            matrix[ i ][ j-1 ], # prev left
                        ) + 1

                    mx = max( mx, matrix[ i ][ j ] )
        
        return mx ** 2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print( f'Max Square: {Solution.maximalSquare( super, matrix )}' )

# Beats 46.24% Runtime, 686ms
# Beats 25.63% Memory, 19.2mb