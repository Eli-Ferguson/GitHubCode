
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

graph2 = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0]
]
graph3 = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def printDiscoveryPath( graph, start ) :
    
    visited = [ start ]
    
    def DFS( graph, currentnode ) :

        for connection in range( len( graph[ currentnode ] ) ) :
            
            if graph[ currentnode ][ connection ] :
                
                if connection not in visited :
                    print( f'At {currentnode} visiting {connection}')
                    visited.append( connection )
                    DFS( graph, connection )
        
    DFS( graph, start )
    
    print( visited, '\n' )

printDiscoveryPath( graph, 0 )
printDiscoveryPath( graph2, 0 )
printDiscoveryPath( graph3, 0 )
