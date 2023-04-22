class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:

        words = []

        for word in queries :
            for testWord in dictionary :

                mistakes = 0

                for i in range( len( word ) ) :

                    if word[ i ] != testWord[ i ] :
                        mistakes += 1
                        if mistakes > 2 :
                            break
                
                if mistakes <= 2 :
                    words.append( word )
                    break

        return words

print( Solution.twoEditWords( super, ["word","note","ants","wood"], ["wood","joke","moat"] ) )