# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        q = [ root ]
        ans = root.val

        while q :
            node = q.pop( 0 )
            ans = node.val

            if node.right : q.append( node.right )
            if node.left : q.append( node.left )
        
        return ans
    
Tree = TreeNode( 1 )
Tree.left = TreeNode( 2 )
Tree.right = TreeNode( 3 )
Tree.left.left = TreeNode( 4 )
Tree.left.right = TreeNode( 5 )
Tree.right.left = TreeNode( 6 )
Tree.right.right = TreeNode( 7 )

print( f'Bottom Left Most Node: {Solution.findBottomLeftValue( super, Tree )}' )

# Beats 54.72% Runtime, 51ms
# Beats 8.26% Memory, 19.6mb