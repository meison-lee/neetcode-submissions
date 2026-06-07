class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, end = 0, len(numbers) - 1;
        
        while (True):
            if (numbers[front] + numbers[end]) > target:
                end -= 1;
            elif (numbers[front] + numbers[end]) < target:
                front += 1;
            else:
                return [front + 1, end + 1];