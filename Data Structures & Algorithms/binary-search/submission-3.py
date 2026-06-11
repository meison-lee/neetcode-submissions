class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # because the array is in ascending order, so we can use binary seacrh
                
        left = 0 
        right = len(nums) - 1
        
        while (right - left) > 1:
            middle = (left + right)//2
            print(left, right, middle)
            if nums[middle] == target: 
                return middle
            elif nums[middle] > target: 
                right = middle
            else : 
                left = middle   
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1