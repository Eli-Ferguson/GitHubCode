class Solution:
    
    def rot90( self, mat ) :
        
        newDepth = len( mat[0] )
        newWidth = len( mat )
                
        rotMat = [ [] for _ in range( newDepth ) ]
                
        for depth in range( len( mat ) ) :
            for width in range( len( mat[ depth ] ) ) :            
                rotMat[width].append( mat[depth][width] )
                
        for row in rotMat :
            row.reverse()
        
        return rotMat
    
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        
        if mat == target : return True
        
        for _ in range( 3 ) :
            
            mat = self.rot90( mat )
            if mat == target : return True
        
        return False
                

print( Solution().findRotation( [ [0,1], [1,0] ], [ [1,0], [0,1] ] ) )
print( Solution().findRotation( [ [0,1], [1,1] ], [ [1,0], [0,1] ] ) )
print( Solution().findRotation( [ [0,0,0], [0,1,0], [1,1,1] ], [ [1,1,1], [0,1,0], [0,0,0] ] ) )

# Beats 72.54% Runtime, 43ms
# Beats 97.54% Memory, 13.8mb