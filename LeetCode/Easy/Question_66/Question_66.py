class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        carry = 1
        end = len( digits ) - 1
        while carry and end >= 0 :

            if digits[ end ] < 9 :
                digits [ end ] += carry
                carry = 0
            else :
                digits[ end ] = 0
                carry = 1
            
            end -= 1
        
        if carry : return [ 1 ] + digits 
        else: return digits
        
digits = [4,3,2,1]

print( f'Plus One Array: {Solution.plusOne( super, digits )}' )

# Beats 80.38% Runtime, 31ms
# Beats 15.49% Memory, 16.2mb