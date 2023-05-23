# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        level = []

        def DFS( root, depth ) :
            if not root : return

            if len( level ) == depth : level.append( [] ) 

            level[ depth ].append( root.val )

            DFS( root.left, depth+1 )
            DFS( root.right, depth+1 )

        DFS( root, 0 )

        return level[ -1 ][ 0 ]

Tree = TreeNode( 1 )
Tree.left = TreeNode( 2 )
Tree.right = TreeNode( 3 )
Tree.left.left = TreeNode( 4 )
Tree.left.right = TreeNode( 5 )
Tree.right.left = TreeNode( 6 )
Tree.right.right = TreeNode( 7 )

print( f'Bottom Left Most Node: {Solution.findBottomLeftValue( super, Tree )}' )

# Beats 60.34% Runtime, 50ms
# Beats 32.49% Memory, 18.8mb