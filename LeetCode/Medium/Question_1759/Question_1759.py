class Solution:
    def countHomogenous(self, s: str) -> int:

        count = 0
        start = 0

        while start < len( s ):

            i = 1

            while start+i < len( s ) :
                if s[ start ] == s[ start + i ] :
                    count += i
                    i+=1
                else : break

            start += i
            count += i

        return count % ( ( 10 ** 9) + 7 )
    
s = "abbcccaa"

print( f'Homogeneous Sub-Strings Count: {Solution.countHomogenous( super, s )}' )    

# Beats 16.88% Runtime, 240ms
# Beats 77.27% Memory, 14.8mb