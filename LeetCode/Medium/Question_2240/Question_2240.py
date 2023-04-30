class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:

        c1 = 0
        count = 0

        while c1 <= total :

            if cost2 > 0 :
                count += int( ( total - c1 ) / cost2 + 1)
            else :
                count += 1

            c1 += cost1

        return count

total = 20
cost1 = 10
cost2 = 5

print( f'Possible Combinations: {Solution.waysToBuyPensPencils( super, total, cost1, cost2 )}' )

# Beats 5.6.3%% Runtime, 1168ms
# Beats 96.48% Memory, 13.8mb