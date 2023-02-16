class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        tmp = nums.copy()
        tmp.sort()

        i = 0
        j = len( tmp ) - 1

        while i < j :

            if tmp[i] + tmp[j] == target : break
            elif tmp[i] + tmp[j] < target : i+=1
            elif tmp[i] + tmp[j] > target : j-=1

        idx1 = nums.index(tmp[i])
        nums[idx1] = -1
        idx2 = nums.index(tmp[j])

        return [ idx1, idx2 ]

print( Solution().twoSum( [2,7,11,15], 9 ) )
print( Solution().twoSum( [3,2,4], 6 ) )
print( Solution().twoSum( [3,3], 6 ) )

# Beats 86.87% Runtime, 60ms
# Beats 92.17% Memory, 14.9mb