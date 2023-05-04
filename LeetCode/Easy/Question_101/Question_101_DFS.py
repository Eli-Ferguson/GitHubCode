# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: TreeNode ) -> bool:
        if not root : return True
        
        def DFS( left, right ) :
            if not left and not right : return 1

            if left and right and left.val == right.val :
                return DFS( left.left, right.right ) and DFS( left.right, right.left )

            return 0

        return DFS( root.left, root.right )

# Beats 10.63% Runtime, 44ms
# Beats 5.63% Memory, 16.4mb