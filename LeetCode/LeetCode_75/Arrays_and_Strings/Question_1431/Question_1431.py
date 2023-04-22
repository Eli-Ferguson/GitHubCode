class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        maxC = max( candies )

        return [ extraCandies + x >= maxC for x in candies ]
  
candies = [2,3,5,1,3]
extraCandies = 3  

print( f'kids with max candies: {Solution.kidsWithCandies( super, candies, extraCandies )}' )

# Beats 98.26% Runtime, 28ms
# Beats 51.16% Memory, 13.8mb