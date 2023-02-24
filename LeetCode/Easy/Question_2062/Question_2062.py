class Solution:

    def containsOnlyVowels( self, partialStr:str ) :
        vowels = [ 'a','e','i','o','u' ]

        for char in partialStr :
            if char not in vowels : return False
        
        for vowel in vowels :
            if not partialStr.__contains__(vowel) : return False
        
        return True


    def countVowelSubstrings(self, word: str) -> int:

        subStrings = []        
        wordList = list( word )

        for i in range( len( word )-4 ) :
            for j in range( i+4, len( word ) ) :
                if self.containsOnlyVowels( wordList[i:j+1] ) :
                    subStrings.append( wordList[i:j+1] )        
        
        return len( subStrings )


print( Solution().countVowelSubstrings( "cuaieuouac" ) )
print( Solution().countVowelSubstrings( "aeiouu" ) )

# Beats 7.77% Runtime, 608ms
# Beats 57.52% Memory, 13.8mb