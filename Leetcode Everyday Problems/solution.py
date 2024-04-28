class Solution(object):
    def maximalRectangle(self, matrix):
        # Check if the matrix is empty or has no rows
        if not matrix or not matrix[0]:
            return 0

        # Get the number of columns in the matrix
        n = len(matrix[0])
        # Initialize a list to store the heights of histogram bars
        heights = [0] * (n + 1)
        # Initialize the maximum area of the rectangle
        max_area = 0

        # Iterate over each row in the matrix
        for row in matrix:
            # Calculate the heights of histogram bars for the current row
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0

            # Initialize a stack with a sentinel value -1
            stack = [-1]
            # Iterate over each column (plus one extra iteration for the last column)
            for i in range(n + 1):
                # While the height of the current column is less than the height of the last element in the stack
                while heights[i] < heights[stack[-1]]:
                    # Calculate the height and width of the rectangle
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    # Update the maximum area if the current area is greater
                    max_area = max(max_area, h * w)
                # Push the current column index onto the stack
                stack.append(i)

        # Return the maximum area of the rectangle
        return max_area

# Test cases
solution = Solution()
matrix1 = [["1","0","1","0","0"],
           ["1","0","1","1","1"],
           ["1","1","1","1","1"],
           ["1","0","0","1","0"]]
print(solution.maximalRectangle(matrix1))  # Output: 6

matrix2 = [["0"]]
print(solution.maximalRectangle(matrix2))  # Output: 0

matrix3 = [["1"]]
print(solution.maximalRectangle(matrix3))  # Output: 1
