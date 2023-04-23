class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:

        # Check for No shift
        lg = len( grid[0] )
        k = k % ( len( grid ) * lg )
        if k == 0 : return grid

        arr = []

        # Flatten grid into a continuous arr
        for row in grid :
            for item in row :
                arr.append( item )
        
        # Splice arr and swap
        arr = arr[-k:] + arr[:-k]

        # Reformat array into grid shape
        row = 0
        for i in range( len( arr ) ) :
            spot = i % lg

            grid[ row ][ spot ] = arr[ i ]

            if i % lg == lg - 1 :
                row += 1
                    
        return grid

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4

print( f'Shifted Grid:\n{Solution.shiftGrid( super, grid, k )}' )

# Beats 90.5% Runtime, 152ms
# Beats 84.23% Memory, 14.2mb