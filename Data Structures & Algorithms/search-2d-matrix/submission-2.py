class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1        

        while left < right:
            middle = (left + right) // 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] < target:
                left = middle + 1
            else:
                right = middle - 1
                
        row = (left+right)//2
        if matrix[row][0] > target:
            row -= 1
            if row < 0: 
                return False
        # if matrix[row][0] < target:
        #     row += 1
        #     if row > len(matrix) - 1: 
        #         return False


        left = 0
        right = len(matrix[row]) - 1
        while left < right:
            middle = (left + right) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return matrix[row][left] == target