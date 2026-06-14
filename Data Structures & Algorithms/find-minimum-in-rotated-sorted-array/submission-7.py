class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1        

        while (left + 1) < right:
            mid = (left + right)//2
            if (nums[mid] > nums[left]) and (nums[mid] < nums[right]):
                return nums[left]
            elif (nums[mid] < nums[left]) and (nums[mid] > nums[right]):
                left = mid + 1
            elif (nums[mid] < nums[left]) and (nums[mid] < nums[right]):
                if (nums[left] - nums[mid]) > (nums[right] - nums[mid]):
                    right = mid
                    left = left + 1
                else:
                    left = mid
                    right = right - 1
            else:
                if (nums[mid] - nums[left]) > (nums[mid] - nums[right]):
                    right = left + 1
                else:
                    left = mid + 1                    
        
        if nums[left] > nums[right]:
            return nums[right]
        else:
            return nums[left]