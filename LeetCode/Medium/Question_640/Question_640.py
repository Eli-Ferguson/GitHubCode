class Solution:

    def simplify( self, partialEquation:str ) :

        xCount = 0
        numberResult = 0
        prevOperation = ''
        
        iIgnore = []

        for i, char in enumerate( partialEquation ) :
        
            if i not in iIgnore :
                        
                if char == 'x' :
                    if prevOperation == '' or prevOperation == '+':
                        xCount+=1
                    else :
                        xCount-=1
                                        
                elif char == '+' or char == '-' :
                    prevOperation = char

                else :
                    numStr = char
                    x = i+1
                                    
                    while x <= len( partialEquation )-1 and partialEquation[ x ] != 'x' and partialEquation[ x ] != '-' and partialEquation[ x ] != '+' :
                        numStr += partialEquation[ x ]
                        iIgnore.append( x )
                        x+=1
                                                        
                    if x > len( partialEquation )-1 : x-=1
                                        
                    if partialEquation[x] == 'x' :                    
                        if prevOperation == '' or prevOperation == '+':
                            xCount += ( int( numStr ) - 1 )
                        else :
                            xCount -= ( int( numStr ) - 1 )
                            
                    else :
                        if prevOperation == '' : numberResult = int( numStr )
                        elif prevOperation == '+' : numberResult += int( numStr )
                        else : numberResult -= int( numStr )
                    
        return xCount, numberResult

    def solveEquation(self, equation: str) -> str:

        splitStr = equation.split('=')
        if len(splitStr) != 2 :
            return 'No solution'
        
        left, right = splitStr[0], splitStr[1]
        
        l_xCount, l_numberResult = self.simplify( left )
        r_xCount, r_numberResult = self.simplify( right )
        
        if l_xCount == r_xCount  and l_numberResult == r_numberResult :
            return 'Infinite solutions'
        elif l_xCount == r_xCount  and l_numberResult != r_numberResult :
            return 'No solution'
            
        
        xCount = 0
        numberResult = 0
        
        if l_xCount > r_xCount :
            xCount = l_xCount - r_xCount
            numberResult = r_numberResult - l_numberResult
        else :
            xCount = r_xCount - l_xCount
            numberResult = l_numberResult - r_numberResult
        
        numberResult = numberResult / xCount
        
        return f'x={numberResult:.0f}'

print( Solution().solveEquation( "2x=x" ) )
print( Solution().solveEquation( "-x=-1" ) )
print( Solution().solveEquation( "x+5-3+x=6+x-2" ) )
print( Solution().solveEquation( "3x=33+22+11" ) )
print( Solution().solveEquation( "2x+3x-6x=x+2" ) )

# Beats 90.74% Runtime, 27ms
# Beats 35.80% Memory, 14.1mb