class Solution(object):
    def findRotateSteps(self, ring, key):
        # Importing defaultdict from collections module
        from collections import defaultdict

        # Helper function to calculate minimum distance between two points on a ring
        def min_distance(p1, p2, n):
            return min(abs(p1 - p2), n - abs(p1 - p2))

        # Length of the ring and the key
        n, m = len(ring), len(key)

        # Storing the positions of each character in the ring
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        # Initializing a 2D array to store the minimum steps required to spell each character in the key
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Initializing the first character in the key
        for i in pos[key[0]]:
            dp[0][i] = min(i, n - i) + 1

        # Calculating the minimum steps for each character in the key
        for i in range(1, m):
            for j in pos[key[i]]:
                for k in pos[key[i - 1]]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + min_distance(j, k, n) + 1)

        # Returning the minimum steps required to spell the entire key
        return min(dp[-1])

# Creating an instance of the Solution class
solution = Solution()

# Test cases
print(solution.findRotateSteps("godding", "gd"))  # Output: 4
print(solution.findRotateSteps("godding", "godding"))  # Output: 13
