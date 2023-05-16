from functools import cache
from math import isqrt

class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:

        @cache
        def isPrime( x ) :
            if x == 1 :
                return False
            if len( [ i for i in range( 2, isqrt( x ) + 1 ) if x % i == 0 ] ) :
                return False
            else :
                return True

        maxPrime = 0

        for i in range( len( nums ) ) :

            if isPrime( nums[ i ][ i ] ) :
                maxPrime = max( maxPrime, nums[ i ][ i ] )
            
            if isPrime( nums[ i ][ -( i + 1 ) ] ) :
                maxPrime = max( maxPrime, nums[ i ][ -( i + 1 ) ] )
                
        return maxPrime
    
nums = [[1,2,3],[5,17,7],[9,11,10]]

print( f'Largest Prime On the Diagonals: {Solution.diagonalPrime( super, nums )}' )
    
# Beats 53.84% Runtime, 239ms
# Beats 5.18% Memory, 17.8mb