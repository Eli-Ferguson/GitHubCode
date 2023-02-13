class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.replace( '-','' )[::-1]
        
        ret = ''

        for i in range( len( s ) ) :
           if (i+1) % k == 0 : ret = ret + s[ i ] + '-'
           else : ret += s[ i ]
           
        ret = ret[::-1]
                
        return ret.removeprefix('-').upper()
        
print( Solution().licenseKeyFormatting( "5F3Z-2e-9-w", 4 ) )
print( Solution().licenseKeyFormatting( "2-5g-3-J", 2 ) )

# Beats 32.5% Runtime, 92ms
# Beats 85.7% Memory, 14.5mb