class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        ret = 0

        for i in range( n ) :
            ret = ret ^ ( start + ( 2 * i ) )
        
        return ret

print( Solution().xorOperation( 5, 0 ) )
print( Solution().xorOperation( 4, 3 ) )

# Beats 99.52% Runtime, 19ms
# Beats 53.21% Memory, 13.9mb