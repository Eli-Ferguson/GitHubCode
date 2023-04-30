# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root : return root

        parentNodes = [ root ]
        root.val = 0

        currLevelNodes = []

        def BFS() :

            nonlocal parentNodes
            nonlocal currLevelNodes
            
            currLevelNodes = [ 0 for _ in range( len( parentNodes ) ) ]
            currLvlSum = 0

            for i in range( len( parentNodes ) ) :

                if parentNodes[ i ].left :
                    val = parentNodes[ i ].left.val

                    currLevelNodes[ i ] += val
                    currLvlSum += val

                if parentNodes[ i ].right :
                    val = parentNodes[ i ].right.val

                    currLevelNodes[ i ] += val
                    currLvlSum += val
            
            for i in range( len( parentNodes ) ) :

                if parentNodes[ i ].left :
                    parentNodes[ i ].left.val = currLvlSum - currLevelNodes[ i ]

                if parentNodes[ i ].right :
                    parentNodes[ i ].right.val = currLvlSum - currLevelNodes[ i ]
            
            tmp = []

            for parent in parentNodes :

                if parent.left : tmp.append( parent.left )
                if parent.right : tmp.append( parent.right )
            
            parentNodes = tmp
            currLevelNodes = []

        while parentNodes != [] :

            BFS()

        return root

# Beats 80.73% Runtime, 1367ms
# Beats 100% Memory, 158.7mb