# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        :param root: root node of a BST.
        :param key: the target value of the node that need to delete from BST.
        :return: root node of the BST with key value node has been deleted.
        """
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # when find the target node,  get the minimum value node on it's right descendant,
            # replace the target node value with the minimum right descendant'value, then continue
            # the recursion to delete the minimum right descendant node.
            if not root.right:
                return root.left
            min_right_node = root.right
            while min_right_node.left:
                min_right_node = min_right_node.left
            root.val = min_right_node.val
            root.right = self.deleteNode(root.right, min_right_node.val)
            return root

        
