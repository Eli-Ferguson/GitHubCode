from functools import cache

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        @cache
        def convert(n, b):
            e = n // b
            q = n % b

            if n == 0:
                return '0'
            elif e == 0:
                return str( q )
            else:
                return convert( e, b ) + str( q )

        def isPal( x ) :
            x = str( x )

            return x == x[::-1]

        base = 2

        while base <= n - 2 :

            if not isPal( convert( n, base ) ) :
                return False
            
            base += 1
        
        return True
    
n = 9

print( f'Strictly Palindromes: {Solution.isStrictlyPalindromic( super, n )}' )

# Beats 27.99% Runtime, 41ms
# Beats 7.4% Memory, 16.4mb