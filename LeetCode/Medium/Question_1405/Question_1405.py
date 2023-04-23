from collections import Counter

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        count = Counter( { 'a':a, 'b':b, 'c':c } )

        # Init
        ret = [':']

        while True :
            
            # Get top two letters
            ( mcc, _ ), ( mcc2, _ ) = count.most_common( 2 )
            
            # Check if previous two chars are mcc
            if ret[ -1 ] == mcc and ret[ -2 ] == mcc :
                # if so swap to second most common char
                mcc = mcc2
            
            # if letter count == 0 end loop
            if not count[ mcc ] : break

            # add char
            ret.append( mcc )
            count[ mcc ] -= 1
        
        # build string excluding init char
        return ''.join( ret[ 1: ] )

a, b, c = 1, 1, 7

print( f'New String = {Solution.longestDiverseString( super, a, b, c )}' )