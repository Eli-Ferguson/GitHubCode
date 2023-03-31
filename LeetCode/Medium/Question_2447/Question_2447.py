from math import gcd
class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        
        answers = 0

        for i in range( len( nums ) ) :

            tmp = nums[i]

            for j in range( i, len( nums ) ) :

                tmp = gcd( tmp, nums[j] )

                if tmp == k : answers += 1
                elif tmp < k : break

        return answers
    
# Beats 86.93% Runtime, 147ms
# Beats 70.59% Memory, 14mb