
class Solution:
    def getMaximumGold(self, grid):
        def dfs(i, j):
            # Base Case: If cell is outside grid or has no gold, return 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            gold = grid[i][j]  # Collect gold from current cell
            grid[i][j] = 0  # Mark current cell as visited
            max_gold = 0
            # Explore neighboring cells (up, down, left, right)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                max_gold = max(max_gold, dfs(i + dx, j + dy))  # Recursively call dfs
            grid[i][j] = gold  # Restore original value of current cell
            return max_gold + gold  # Return maximum gold collected from current cell onwards

        max_gold = 0
        # Iterate over each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:  # If cell has gold, start collecting from it
                    max_gold = max(max_gold, dfs(i, j))  # Call dfs to find maximum gold from current cell
        return max_gold  # Return maximum gold that can be collected

# Example usage
grid1 = [[0,6,0],[5,8,7],[0,9,0]]
grid2 = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]

sol = Solution()
print(sol.getMaximumGold(grid1))  # Output: 24
print(sol.getMaximumGold(grid2))  # Output: 28
