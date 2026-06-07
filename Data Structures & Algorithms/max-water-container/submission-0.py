class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f, e = 0, len(heights) - 1
        ans = 0
        while (f < e):
            height = min(heights[f], heights[e])
            ans = max(ans, height*(e-f))
            if height == heights[f]: f += 1
            if height == heights[e]: e -= 1
        return ans