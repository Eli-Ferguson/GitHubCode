from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:

        total = 0

        for _, val in Counter( nums ).most_common() :
            if val == 1 :
                break
            else :
                total += ( val**2 - val ) / 2

        return int( total )
    
nums = [1,2,3,1,1,3]

print( f'Identical Pairs: {Solution.numIdenticalPairs( super, nums )}' )

# Beats 6.7% Runtime, 55ms
# Beats 13.7% Memory, 16.3mb