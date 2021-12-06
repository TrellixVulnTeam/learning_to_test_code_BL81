from typing import List, Dict

# see: 
# https://leetcode.com/problems/maximal-square/discuss/1458252/PyPy3-Solution-using-only-for-loops-w-comments

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # Init
        m = len(matrix)
        n = len(matrix[0])
        max_len = 0
        
        # Convert matrix value of string to int
        for row in range(m):
            for col in range(n):
                matrix[row][col] = int(matrix[row][col])
        
        # Scan first row
        for col in range(n):
            max_len = max(max_len, matrix[0][col])
            
        # Scan first column
        for row in range(m):
            max_len = max(max_len, matrix[row][0])
        
        # For each row starting from second row
        for i in range(1,m):
            
            # For each col starting from second column
            for j in range(1,n):
                
                # If the current element is non-zero
                if matrix[i][j]:
                    
                    # If all three of it's adjacent elements are non-zero
                    # Three elements are:
                    # a) element in the previous row "[i-1][j]"
                    # b) element in the previous column "[i][j-1]"
                    # c) element in previous diagonal "[i-1][j-1]"
                    if matrix[i-1][j] and matrix[i][j-1] and matrix[i-1][j-1]:
                        print('3 conditions met')
                        print(matrix)
                        
                        # Get the minimum of all three adjacent elements and add one to it
                        # This updates length of the element w.r.t how many adjacent ones
                        # are available in the original matrix
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                        print(matrix)
                    
                    # Calc max len w.r.t the updated length of the current element
                    max_len = max(max_len, matrix[i][j])
                        
                    
        return max_len**2 # Area of a square of length "l" is l*l = l^2
    
if __name__ == "__main__":
    matrix = [
        [1, 1, 0],
        [1, 1, 0]
    ]
    solution = Solution()
    print(solution.maximalSquare(matrix))