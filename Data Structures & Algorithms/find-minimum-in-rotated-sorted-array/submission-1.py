class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1        

        while (left + 1) < right:
            mid = (left + right)//2
            if (nums[mid] > nums[left]) and (nums[mid] < nums[right]):
                right = mid
            elif (nums[mid] < nums[left]) and (nums[mid] > nums[right]):
                left = mid
            elif (nums[mid] < nums[left]) and (nums[mid] < nums[right]):
                if (nums[left] - nums[mid]) > (nums[right] - nums[mid]):
                    right = mid
                else:
                    left = mid
            else:
                if (nums[mid] - nums[left]) > (nums[mid] - nums[right]):
                    right = mid
                else:
                    left = mid
        
        if nums[left] > nums[right]:
            return nums[right]
        else:
            return nums[left]