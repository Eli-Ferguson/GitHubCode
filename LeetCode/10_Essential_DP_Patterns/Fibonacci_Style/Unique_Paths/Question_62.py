class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # initialize 2D dp arr
        dp = [ [ 0 for _ in range( n+1 ) ] for _ in range( m+1 ) ]

        def dynamic( row, column ) :

            # At the final corner
            if row == m and column == n :
                return 1

            # at the bottom of the grid
            elif row == m :

                # if right unexplored
                if dp[ row ][ column+1 ] == 0 :
                    dp[ row ][ column+1 ] = dynamic( row, column+1 )
                
                # return val to the right
                return dp[ row ][ column+1 ]

            # at the end of the row
            elif column == n :
                
                # if down unexplored
                if dp[ row+1 ][ column ] == 0 :
                    dp[ row+1 ][ column ] = dynamic( row+1, column )
                
                # return val below
                return dp[ row+1 ][ column ]
            
            else :
                
                # if right unexplored
                if dp[ row ][ column+1 ] == 0 :
                    dp[ row ][ column+1 ] = dynamic( row, column+1 )
                
                # if down unexplored
                if dp[ row+1 ][ column ] == 0 :
                    dp[ row+1 ][ column ] = dynamic( row+1, column )
                
                # return right + down
                return dp[ row ][ column+1 ] + dp[ row+1 ][ column ]
        
        # return val from start, 
        return dynamic( 1, 1 )
    
m = 3
n = 7

print( f'Unique paths for grid size {m}x{n}: {Solution.uniquePaths( super, m, n )}' )

# Beats 74.23% Runtime, 31ms
# Beats 5.7% Memory, 16.5mb