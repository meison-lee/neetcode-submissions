class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0;
        # left, right = 0, len(height) - 1;
        # max_left, max_right = 0, 0;

        # while (left < right):
        #     if (height[left] < height[right]):
        #         max_left = max(max_left, height[left])
        #         ans += max_left - height[left]
        #         left += 1
        #     else :
        #         max_right = max(max_right, height[right])
        #         ans += max_right - height[right]
        #         right -= 1

        left_matric, right_matric = [0] * len(height), [0] * len(height);
        max_left, max_right = 0, 0;
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            max_right = max(max_right, height[len(height) - 1 - i])
            left_matric[i] = max_left
            right_matric[len(height) - 1 - i] = max_right
        
        for i in range(len(height)):
            ans += min(left_matric[i], right_matric[i]) - height[i]

        return ans