# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        current_node = root

        stack = []
        done = False
        sum = 0
        while not done:

            if current_node != None:
                stack.append(current_node)
                current_node = current_node.left

            else:
                if len(stack) != 0:
                    current_node = stack.pop()

                    if current_node.val >= low and current_node.val <= high:
                        sum = sum + current_node.val

                    current_node = current_node.right
                else:
                    done = True

        return sum