class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        
        summ = 0

        s, e = 0, len( nums )-1

        while e - s > 0 :
            summ += int( str( nums[ s ] ) + str( nums[ e ] ) )
            s += 1
            e -= 1
            
        if s == e : return summ + nums[ s ]
        else : return summ
   
nums = [5,14,13,8,12]
        
print( f'Array Concat Value: {Solution.findTheArrayConcVal( super, nums )}' )

# Beats 49.75% Runtime, 473ms
# Beats 93.57% Memory, 32.3mb