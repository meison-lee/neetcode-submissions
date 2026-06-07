class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # using stack
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            target = temperatures[i]
            while(stack and temperatures[stack[-1]] < target):
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        while (stack):
            res[stack.pop()] = 0

        return res
