class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:

        A = [ 0 ] * 8
        B = [ 0 ] * 8

        for i in range( len( moves ) ) :

            row, col = moves[ i ]
            
            player = A if i % 2 == 0 else B

            player[ row ] += 1
            player[ col+3 ] += 1

            if row == col :
                player[ 6 ] += 1
            if row == 2-col :
                player[ 7 ] += 1

        for i in range( 8 ) :
            if A[ i ] == 3 : return 'A'
            if B[ i ] == 3 : return 'B'
        
        return 'Draw' if len( moves ) == 9 else 'Pending'
    
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]

print( f'Winner Of Tic Tac Toe: {Solution.tictactoe( super, moves )}' )

# Beats 25.29% Runtime, 45ms
# Beats 23.77% Memory, 16.2mb