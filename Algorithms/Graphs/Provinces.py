
graph = [ [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1] ]

class Solution :
    def provinces( graph ) :
        
        def dfs( graph, visited, i ) :
                        
            if i in visited :
                return 0
            
            visited.add( i )
            
            for j in range( len( graph[ i ] ) ) :
                if graph[i][j] : 
                    print( f'At node {i} visiting {j}')
                    dfs( graph, visited, j )
            
            return 1
        
        visited = set()
        pCount = 0
        
        for i in range( len( graph ) ) :
            pCount += dfs( graph, visited, i)
            print( pCount )
        
        print( f'Total Provinces : {pCount}' )
            
Solution.provinces( graph )