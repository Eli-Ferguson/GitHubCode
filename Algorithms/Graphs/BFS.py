
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
    q = []
    
    def BFS( graph, currentNode ) :
                
        for connection in range( len( graph[ currentNode ] ) ) :
            
            if graph[ currentNode ][ connection ] :
                
                if connection not in visited :
                    
                    visited.append( connection )
                    q.append( connection )
        
        print( f'Current node: {currentNode}\t\tQueue : {q}' )
        if q : BFS( graph, q.pop( 0 ) )
        
        
    BFS( graph, start )
    
    print( visited )

# printDiscoveryPath( graph, 0 )
# printDiscoveryPath( graph2, 0 )
printDiscoveryPath( graph3, 0 )
