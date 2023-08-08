# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :param root: root node of a binary tree.
        :return: a list contrain the preorder traversal of nodes values.
        """
        # solve this quesion by recursion.
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + \
                   self.preorderTraversal(root.right)


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :param root: root node of a binary tree.
        :return: a list contrain the preorder traversal of nodes values.
        """
        # solve this quesion by stack and iteration.
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res 
