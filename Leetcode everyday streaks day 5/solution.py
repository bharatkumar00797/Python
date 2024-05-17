# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Define a class for the solution
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        # Base case: if the root is None, return None
        if not root:
            return None
        
        # Recursively call the function on the left and right children
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # If the current node becomes a leaf node and its value is the target, return None
        if not root.left and not root.right and root.val == target:
            return None
        
        return root

# Example usage
def print_tree(root):
    """Helper function to print the tree level by level (for testing purposes)"""
    if not root:
        return "Empty"
    
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for clearer output
    while result and result[-1] is None:
        result.pop()
    return result

# Construct a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

# Create an instance of the Solution class
solution = Solution()
# Remove leaf nodes with value 2 from the tree
new_root = solution.removeLeafNodes(root, 2)

# Printing the resulting tree
print(print_tree(new_root))  # Output should be [1, None, 3, None, 4]
