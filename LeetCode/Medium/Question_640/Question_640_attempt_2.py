class Solution:
    def solveEquation(self, equation: str) -> str:

        i = 0
        l_xCount = 0
        l_numResult = 0
        r_xCount = 0
        r_numResult = 0        
        
        operation = ''
        numStr = ''

        while equation[i] != '=' :
            
            if equation[i].isnumeric() :
                numStr += equation[i]
                
            elif equation[i] == 'x' :
                if operation == '' or operation == '+' : l_xCount = l_xCount + int( numStr ) if numStr != '' else l_xCount + 1
                else : l_xCount = l_xCount - int( numStr ) if numStr != '' else l_xCount - 1
                
                numStr = ''
            else :
                
                if numStr != '' :
                    if operation == '+' or operation == '' : l_numResult += int( numStr )
                    else : l_numResult -= int( numStr )
                
                numStr = ''
                operation = equation[i]
            
            i+=1
        
        if numStr != '' :
            if operation == '+' or operation == '' : l_numResult += int( numStr )
            else : l_numResult -= int( numStr )
            numStr = ''
            
        operation = ''        
        i+=1
                
        while i < len( equation ) :
                        
            if equation[i].isnumeric() :
                numStr += equation[i]
                
            elif equation[i] == 'x' :
                if operation == '' or operation == '+' : r_xCount = r_xCount + int( numStr ) if numStr != '' else r_xCount + 1
                else : r_xCount = r_xCount - int( numStr ) if numStr != '' else r_xCount - 1
                
                numStr = ''
            else :
                
                if numStr != '' :
                    if operation == '+' or operation == '' : r_numResult += int( numStr )
                    else : r_numResult -= int( numStr )
                
                numStr = ''
                operation = equation[i]
            
            i+=1
        
        if numStr != '' :
            if operation == '+' or operation == '' : r_numResult += int( numStr )
            else : r_numResult -= int( numStr )
                    
                
        if l_xCount == r_xCount and l_numResult == r_numResult :
            return 'Infinite solutions'
        elif l_xCount == r_xCount and l_numResult != r_numResult :
            return 'No solution'
        
        xCount = 0
        numResult = 0
                
        if l_xCount > r_xCount :
            xCount = l_xCount - r_xCount
            numResult = r_numResult - l_numResult
        else :
            xCount = r_xCount - l_xCount
            numResult = l_numResult - r_numResult
        
        numResult = numResult / xCount
        
        return f'x={round(numResult)}'
            
            
print( Solution().solveEquation( "x+5-3+x=6+x-2" ) )
print( Solution().solveEquation( "22x+1=x-1" ) )
print( Solution().solveEquation( "x=x+2" ) )

# Beats 90.74% Runtime, 27ms
# Beats 80.86% Memory, 13.9mb