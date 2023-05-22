# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:

    def __init__(self, root: TreeNode):
        self.contains = {}

        if root != [] :
            root.val = 0
        
        self.fill( root )

    def fill( self, root ) :

        self.contains[ root.val ] = 1

        if root.left != None :
            root.left.val = 2 * root.val + 1
            self.fill( root.left )

        if root.right != None :
            root.right.val = 2 * root.val + 2
            self.fill( root.right )

    def find(self, target: int) -> bool:

        if target in self.contains : return True
        else : return False
        
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
###################################################################
Tree = TreeNode( -1 )
Tree.left = TreeNode( -1 )
Tree.right = TreeNode( -1 )
Tree.left.left = TreeNode( -1 )
Tree.left.right = TreeNode( -1 )
Tree.right.left = TreeNode( -1 )
Tree.right.right = TreeNode( -1 )

FindElements_ = FindElements( Tree )

nums = [ 1, 5, 8 ]

print( f'Finding {nums} : {[FindElements_.find( num ) for num in nums ]}' )

# Beats 47.46% Runtime, 96ms
# Beats 32.63% Memory, 20.3mb