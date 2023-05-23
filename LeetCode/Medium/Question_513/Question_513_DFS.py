# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        def DFS( root, depth ) :

            LMV_LeftBranch, L_depth = root.val, depth
            LMV_RightBranch, R_depth = root.val, depth

            if root.left :
                LMV_LeftBranch, L_depth = DFS( root.left, depth+1 )
            
            if root.right :
                LMV_RightBranch, R_depth = DFS( root.right, depth+1 )
            
            if L_depth >= R_depth :
                return LMV_LeftBranch, L_depth
            else :
                return LMV_RightBranch, R_depth
        
        return DFS( root, 0 )[ 0 ]
        

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