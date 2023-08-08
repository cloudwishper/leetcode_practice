# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        :param root: root node of a binary tree.
        :return: return True if input tree is BST otherwise False
        """
        def is_valid_binary_serach_tree(node: Optional[TreeNode], 
                                        left_bound: float,
                                        right_bound: float) -> bool:
            if node is None:
                return True
            if node.val <= left_bound or node.val >= right_bound:
                return False
            else:
                left_is_valid = is_valid_binary_serach_tree(node.left, left_bound, node.val)
                right_is_valid = is_valid_binary_serach_tree(node.right, node.val, right_bound)
                return left_is_valid and right_is_valid

            
        return is_valid_binary_serach_tree(root, -float('inf'), float('inf'))
