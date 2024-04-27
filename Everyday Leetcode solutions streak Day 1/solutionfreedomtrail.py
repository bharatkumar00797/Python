class Solution(object):
    def findRotateSteps(self, ring, key):
        from collections import defaultdict

        def min_distance(p1, p2, n):
            return min(abs(p1 - p2), n - abs(p1 - p2))

        n, m = len(ring), len(key)
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        dp = [[float('inf')] * n for _ in range(m)]
        for i in pos[key[0]]:
            dp[0][i] = min(i, n - i) + 1

        for i in range(1, m):
            for j in pos[key[i]]:
                for k in pos[key[i - 1]]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + min_distance(j, k, n) + 1)

        return min(dp[-1])

# Test cases
solution = Solution()
print(solution.findRotateSteps("godding", "gd"))  # Output: 4
print(solution.findRotateSteps("godding", "godding"))  # Output: 13
