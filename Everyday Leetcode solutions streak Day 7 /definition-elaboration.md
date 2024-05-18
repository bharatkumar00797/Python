Detailed Explanation:

TreeNode Class:

__init__(self, val=0, left=None, right=None): Initializes a node with a given value and optional left and right children. The default value is 0, and the default children are None.
Solution Class:

distributeCoins(self, root): This method calculates the minimum number of moves required to balance the coins in the binary tree.

DFS Helper Function:

dfs(node): A helper function that performs a depth-first search on the binary tree.

Base Case: If the node is None, return 0 (indicating no excess coins to move).

Recursive Case: Recursively call dfs on the left and right children to calculate their excess coins.

Moves Calculation: Add the absolute values of left and right to self.moves, representing the total moves needed to balance the coins at this node.

Net Coins Calculation: Return the net number of coins to be moved to the parent node. This is calculated as node.val + left + right - 1, representing the current node's value plus the left and right excess coins minus the coin needed for the node itself.

Example Usage:

Constructs two sample binary trees and uses the distributeCoins method to calculate and print the number of moves required for each tree.
