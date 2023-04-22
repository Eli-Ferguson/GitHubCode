class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        # If new color == start color, return
        if image[ sr ][ sc ] == color : return image

        # Get starting color
        startingColor = image[ sr ][ sc ]

        # Queue for BFS
        q = [ [ sr, sc ] ]
        
        # list of Nodes visited
        visited = [ [ sr, sc ] ]

        def BFS( q ) :

            node = q.pop( 0 )

            if image[ node[0] ][ node[1] ] == startingColor:
                image[ node[0] ][ node[1] ] = color
            
            # above
            if node[0] > 0 and image[ node[0] - 1 ][ node[1] ] == startingColor :

                if [ node[0] - 1, node[1] ] not in visited :
                    q.append( [ node[0] - 1, node[1] ] )
                    visited.append( [ node[0] - 1, node[1] ] )
            
            # below
            if node[0] < len( image ) - 1 and image[ node[0] + 1 ][ node[1] ] == startingColor :

                if [ node[0] + 1, node[1] ] not in visited :
                    q.append( [ node[0] + 1, node[1] ] )
                    visited.append( [ node[0] + 1, node[1] ] )

            # left
            if node[1] > 0 and image[ node[0] ][ node[1] - 1 ] == startingColor :

                if [ node[0], node[1] - 1 ] not in visited :
                    q.append( [ node[0], node[1] - 1 ] )
                    visited.append( [ node[0], node[1] - 1 ] )
            
            # right
            if node[1] < len( image[0] ) - 1 and image[ node[0] ][ node[1] + 1 ] == startingColor :

                if [ node[0], node[1] + 1 ] not in visited :
                    q.append( [ node[0], node[1] + 1 ] )
                    visited.append( [ node[0], node[1] + 1 ] )
        
        # Avoids Recursion
        while q != [] : BFS( q )

        return image

img = [[1,1,1],[1,1,0],[1,0,1]]

print( 'Original' )
[ print( row ) for row in img ]
print( 'New' )
[ print( row ) for row in Solution.floodFill( super, img, 1, 1, 2 ) ]


# Beats 93.34% Runtime, 70ms
# Beats 83.11% Memory, 14mb