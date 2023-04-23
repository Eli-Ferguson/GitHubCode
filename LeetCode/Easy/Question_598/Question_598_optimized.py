class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:

        if not ops : return m * n
    
        lmin, rmin = ops[0]

        for x, y in ops :
            if x < lmin : lmin = x
            if y < rmin : rmin = y

        return lmin * rmin

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]

print( f'Number Of Max Tiles: {Solution.maxCount( super, m, n, ops )}' )

# Beats 99.61% Runtime, 55ms
# Beats 17.88% Memory, 16.1mb