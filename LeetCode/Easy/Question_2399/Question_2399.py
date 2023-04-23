class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:

        dist = [ -1 ] * 26

        idx = 0
        for i in range( len( s ) ) :

            idx = ord( s[ i ] ) - 97

            if dist[ idx ] != -1 :
                if i - dist[ idx ] - 1 != distance[ idx ] :
                    return False
            else :
                dist[ idx ] = i

        return True

s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print( f'Distance Checks: {Solution.checkDistances( super, s, distance )}' )

# Beats 87.46% Runtime, 39ms
# Beats 97.19% Memory, 13.7mb