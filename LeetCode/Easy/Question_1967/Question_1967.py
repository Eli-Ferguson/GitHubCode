class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:

        return len( [ 0 for pat in patterns if pat in word ] )
    
patterns = ["a","b","c"]
word = "aaaaabbbbb"    

print( f"Substring Count : {Solution.numOfStrings( super, patterns, word )}" )

# Beats 42.26% Runtime, 39ms
# Beats 60.3% Memory, 13.8mb