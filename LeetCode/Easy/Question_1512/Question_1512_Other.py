class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:

        nums.sort()

        start = 0
        end = 0

        total = 0

        while start < len( nums ) :
            
            count = 0
            while end < len( nums ) and nums[ start ] == nums[ end ] :
                end += 1
                count += 1

            start += count
            end = start

            while count > 1 :
                count -= 1
                total += count

        return total
    
nums = [1,2,3,1,1,3]

print( f'Identical Pairs: {Solution.numIdenticalPairs( super, nums )}' )

# Beats 19.3% Runtime, 46ms
# Beats 13.7% Memory, 16.4mb