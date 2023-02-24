class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:

        xyz = [a,b,c]
        xyz.sort()
        a,b,c = xyz


        maxMoves = 0
        minMoves = 0

        ba = abs( b-a )
        cb = abs( c-b )

        if ba != 1 :
            maxMoves += ba-1
            minMoves += 1
                
        if cb != 1 :
            maxMoves += cb-1
            minMoves += 1
    
        if ba == 2 or cb == 2 :
            minMoves = 1
        
        return [ minMoves, maxMoves ]

print( Solution().numMovesStones( a = 1, b = 2, c = 5 ) )
print( Solution().numMovesStones( a = 4, b = 3, c = 2 ) )
print( Solution().numMovesStones( a = 3, b = 5, c = 1 ) )

# Beats 54.58% Runtime, 34ms
# Beats 73.39% Memory, 13.9mb