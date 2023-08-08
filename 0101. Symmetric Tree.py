# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        :param root: root node of a binary tree.
        :return: return True if the input tree is a mirror of itself , otherwise False
        """
        def compare(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return compare(node1.left, node2.right) & compare(node2.left, node1.right)
        
        if not root:
            return True
        else:
            return compare(root.left, root.right)
