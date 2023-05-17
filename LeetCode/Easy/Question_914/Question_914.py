from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:

        counts = list( Counter( deck ).values() )

        if gcd( *counts ) > 1 : return True
        else : return False
        
deck = [1,2,3,4,4,3,2,1]

print( f'Has Group Size X: {Solution.hasGroupsSizeX( super, deck )}' )
        
# Beats 69.33% Runtime, 135ms
# Beats 23.84% Memory, 16.6mb