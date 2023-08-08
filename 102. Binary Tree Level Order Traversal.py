# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        :param root: root node of a binary tree.
        :return: list of the level order traversal of its nodes' values.
        """
        queue = [root] if root else []
        res = []

        while queue:
            result_single_level = []
            next_level_queue = []
            for node in queue:
                result_single_level.append(node.val)
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            res.append(result_single_level)
            queue = next_level_queue
                
        return res
