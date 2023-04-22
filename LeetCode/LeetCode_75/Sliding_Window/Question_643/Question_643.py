class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        maxSum = sum( nums[ :k ] )
        currSum = maxSum

        for i in range( len( nums ) - k ) :

            currSum += ( nums[ i + k ] - nums[ i ] )

            if currSum > maxSum : maxSum = currSum
        
        return maxSum / k

nums = [1,12,-5,-6,50,3]
k = 4

print( f'MaxSum: {Solution.findMaxAverage( super, nums, k )}' )

# Beats 99.12% Runtime, 1141ms
# Beats 37.74% Memory, 26.2mb