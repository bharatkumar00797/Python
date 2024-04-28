This code defines a class `Solution` with a method `maximalRectangle` that calculates the area of the largest rectangle containing only 1's in a binary matrix. Here's a step-by-step explanation of the code:

1. `maximalRectangle(self, matrix)`:
   - This method takes a binary matrix `matrix` as input and returns an integer, which is the area of the largest rectangle containing only 1's in the matrix.

2. `if not matrix or not matrix[0]: return 0`:
   - If the input matrix is empty or has no rows, the method returns 0 as there are no rectangles possible.

3. `n = len(matrix[0])`:
   - `n` is initialized to the number of columns in the matrix. This will be used to iterate over the columns.

4. `heights = [0] * (n + 1)`:
   - `heights` is initialized as a list of zeros with a length of `n + 1`. This list will store the height of the histogram bars for each column.

5. `max_area = 0`:
   - `max_area` is initialized to 0. This variable will store the maximum area of the rectangle found so far.

6. Nested loop to iterate over each row and column in the matrix:
   - For each row in the matrix, the code calculates the heights of the histogram bars for that row. If the element in the matrix is '1', the height is incremented by 1. Otherwise, it is reset to 0.

7. `stack = [-1]`:
   - Initialize a stack with a sentinel value -1. This stack will be used to keep track of the indices of the histogram bars.

8. Nested loop to calculate the maximum area:
   - For each column, the code calculates the maximum area of the rectangle that can be formed ending at that column. It does this by popping elements from the stack until the height of the current column is greater than or equal to the height of the last element popped from the stack. For each popped element, it calculates the area of the rectangle and updates `max_area` if the area is greater.

9. Return `max_area`:
   - Finally, the method returns `max_area`, which is the area of the largest rectangle containing only 1's in the matrix.

10. Test cases:
    - The code includes test cases where it creates instances of the `Solution` class and calls the `maximalRectangle` method with different input matrices to demonstrate its functionality.
