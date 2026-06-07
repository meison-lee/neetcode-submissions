class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)) :
            if (i > 0 and nums[i] == nums[i-1]): continue;
            front, end = i + 1, len(nums) - 1   

            while (front < end):
                if (nums[i] + nums[front] + nums[end] == 0):
                    res.append([nums[i], nums[front], nums[end]])
                    front += 1
                    end -= 1
                elif (nums[i] + nums[front] + nums[end] < 0):
                    front += 1
                else:
                    end -= 1
                if (front > i + 1 and nums[front] == nums[front-1]): front += 1
                if (end < len(nums) - 1 and nums[end] == nums[end+1]): end -= 1
        return res