class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        s = list( s )
        vowels = [ 'a', 'e', 'i', 'o', 'u' ]

        maxVowels = sum( [ 1 for letter in range( k ) if s[ letter ] in vowels ] )
        currVowels = maxVowels + 0

        for i in range( len( s ) - k ) :

            if s[ i + k ] in vowels : currVowels += 1
            if s[ i ] in vowels : currVowels -= 1

            maxVowels = max( maxVowels, currVowels )
        
        return maxVowels

testStr = "abciiidef"
k = 3

# print( f'Max Vowels: {Solution.maxVowels( super, testStr, k )}' )

# Beats 78.82% Runtime, 166ms
# Beats 10.18% Memory, 15.6mb