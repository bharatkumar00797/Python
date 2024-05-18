# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with a value and optional left and right children
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Initialize the total number of moves required to zero
        self.moves = 0
        
        def dfs(node):
            """
            Depth-first search helper function to calculate the number of moves required.
            :type node: TreeNode
            :rtype: int
            """
            if not node:
                # If the node is None, return 0 (no excess coins to move)
                return 0
            
            # Recursively solve for the left subtree
            left = dfs(node.left)
            # Recursively solve for the right subtree
            right = dfs(node.right)
            
            # Calculate the number of moves needed by summing the absolute values of left and right
            # Each absolute value represents the number of moves needed to balance the coins
            self.moves += abs(left) + abs(right)
            
            # Return the net number of coins to be moved to the parent
            # This is the current node's value plus the left and right excess coins minus 1 (the node itself)
            return node.val + left + right - 1
        
        # Start the DFS from the root of the tree
        dfs(root)
        
        # Return the total number of moves calculated
        return self.moves

# Example usage

# Constructing the binary tree [3,0,0]
#        3
#       / \
#      0   0
root1 = TreeNode(3)
root1.left = TreeNode(0)
root1.right = TreeNode(0)

# Creating an instance of the Solution class
solution = Solution()
# Calling the distributeCoins method and printing the result
print(solution.distributeCoins(root1))  # Output: 2

# Constructing the binary tree [0,3,0]
#        0
#       / \
#      3   0
root2 = TreeNode(0)
root2.left = TreeNode(3)
root2.right = TreeNode(0)

# Calling the distributeCoins method with the second tree and printing the result
print(solution.distributeCoins(root2))  # Output: 3
