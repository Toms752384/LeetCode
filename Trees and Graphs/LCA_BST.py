# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find which is bigger
        smaller_node_val, bigger_node_Val = 0, 0
        if p.val >= q.val:
            smaller_node_val = q.val
            bigger_node_Val = p.val
        else:
            smaller_node_val = p.val
            bigger_node_Val = q.val
        
        # handle edge case - both are the same
        if smaller_node_val == bigger_node_Val:
            return p

        # define binary search algorithm
        def binary_search(root: TreeNode):
            # check if LCA found
            cur_value = root.val
            if smaller_node_val <= cur_value <= bigger_node_Val:
                return root
            # choose path to proceed
            if cur_value > bigger_node_Val:
                return binary_search(root.left)
            else:
                return binary_search(root.right)
             
        # start dfs
        return binary_search(root)