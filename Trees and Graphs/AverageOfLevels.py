# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        # algorithm - use BFS for traversing, but add a tuple each time: (node, level)
        # initialize variables
        averages = []
        sum_for_average = 0.0
        counter_for_average = 0.0
        current_level = 0
        
        # edge cases
        if root is None: # empty tree
            return None
        # traversre the tree
        queue = deque()
        queue.append((root, 0)) # add the first element
        while(queue): # BFS
            # pop the next in line
            cur_node, child_level = queue.popleft()

            # calculate average if reached next level
            if child_level > current_level:
                res = float(sum_for_average / counter_for_average)
                averages.append(res)

                # initialize the variables
                current_level = child_level
                sum_for_average = 0.0
                counter_for_average = 0.0

            # add to sum and counter
            counter_for_average += 1.0
            sum_for_average += cur_node.val
            
            # continue with children
            if cur_node.left != None:
                queue.append((cur_node.left, child_level + 1))
            if cur_node.right != None:
                queue.append((cur_node.right, child_level + 1))
        
        # handle the last average
        if counter_for_average > 0:
            res = float(sum_for_average / counter_for_average)
            averages.append(res)

        return averages
        