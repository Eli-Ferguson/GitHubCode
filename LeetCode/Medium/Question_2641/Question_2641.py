# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root : return root
        
        # Root is Always 0 
        root.val = 0

        # Nodes from the depth above current
        parentNodes = [ root ]

        # Nodes at a depth
        currLevelNodes = []

        def BFS() :

            nonlocal parentNodes
            nonlocal currLevelNodes
            
            # Initialize a list of len parents full of zeros
            currLevelNodes = [ 0 for _ in range( len( parentNodes ) ) ]

            # Set current sum to 0
            currLvlSum = 0

            # Check each parent node for children adjusting values for
            # curr nodes and curr sum
            for i in range( len( parentNodes ) ) :

                if parentNodes[ i ].left :
                    val = parentNodes[ i ].left.val

                    currLevelNodes[ i ] += val
                    currLvlSum += val

                if parentNodes[ i ].right :
                    val = parentNodes[ i ].right.val

                    currLevelNodes[ i ] += val
                    currLvlSum += val
            
            # For each parent node set the children values in-place to
            # the curr lvl total sum - the children nodes sum
            for i in range( len( parentNodes ) ) :

                if parentNodes[ i ].left :
                    parentNodes[ i ].left.val = currLvlSum - currLevelNodes[ i ]

                if parentNodes[ i ].right :
                    parentNodes[ i ].right.val = currLvlSum - currLevelNodes[ i ]

            # Reset the parentnodes to the new child nodes
            tmp = []

            for parent in parentNodes :

                if parent.left : tmp.append( parent.left )
                if parent.right : tmp.append( parent.right )
            
            parentNodes = tmp

        # Iterate while there are still parentNodes
        while parentNodes != [] : BFS()

        # Since we replace values in-place, return the original root
        return root

            

# Beats 84.54% Runtime, 1347ms
# Beats 100% Memory, 158.7mb