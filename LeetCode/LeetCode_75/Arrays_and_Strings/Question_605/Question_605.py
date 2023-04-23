class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        if not n : return True

        for i in range( len( flowerbed ) ) :

            if flowerbed[ i ] == 0 :
                if i > 0 and flowerbed[ i - 1 ] :
                    pass
                elif i < ( len( flowerbed ) - 1 ) and flowerbed[ i + 1 ] :
                    pass
                else :
                    flowerbed[ i ] = 1
                    n -= 1
                    if not n : return True
        
        return False
        
flowerbed = [1,0,0,0,1]
n = 1

print( f'Can fit flowers : {Solution.canPlaceFlowers( super, flowerbed, n )}' )

# Beats 86.24% Runtime, 158ms
# Beats 63.23% Memory, 13.8mb