from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        # Create a defaultdict to store the adjacency list representation of the tree
        graph = defaultdict(list)
        # Populate the graph with the given edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize two lists, count and res, to store count of nodes and sum of distances for each node
        count = [1] * n
        res = [0] * n

        # Helper function to perform depth-first search (DFS) to calculate count and sum of distances
        def dfs(node, parent):
            # Traverse through the children of the current node
            for child in graph[node]:
                # Skip the parent node
                if child != parent:
                    # Recursive DFS to calculate count and sum of distances for the child node
                    dfs(child, node)
                    # Update count of nodes for the current node
                    count[node] += count[child]
                    # Update sum of distances for the current node
                    res[node] += res[child] + count[child]

        # Helper function to update sum of distances for each node after initial calculation
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # Update sum of distances for the child node
                    res[child] = res[node] - count[child] + n - count[child]
                    # Recursive DFS for the child node
                    dfs2(child, node)

        # Perform DFS from the root node (node 0)
        dfs(0, -1)
        # Update sum of distances for each node based on the initial calculation
        dfs2(0, -1)

        # Return the calculated sum of distances for each node
        return res

# Example usage
solution = Solution()
print(solution.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))  # Output: [8,12,6,10,10,10]
print(solution.sumOfDistancesInTree(1, []))  # Output: [0]
print(solution.sumOfDistancesInTree(2, [[1,0]]))  # Output: [1,1]
