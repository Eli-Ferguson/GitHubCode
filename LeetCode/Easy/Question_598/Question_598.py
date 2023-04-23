class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:

        if not ops : return m * n
        
        l, r = zip( * ops )

        return min( l ) * min( r )

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]

print( f'Number Of Max Tiles: {Solution.maxCount( super, m, n, ops )}' )

# Beats 74.42% Runtime, 69ms
# Beats 5.70% Memory, 16.2mb