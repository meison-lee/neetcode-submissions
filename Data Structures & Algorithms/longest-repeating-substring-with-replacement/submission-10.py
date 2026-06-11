class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)        
        maxLength = 0
        
        for c in charSet:            
            left = replaceCount = 0       
            for i in range(len(s)):                
                if s[i] != c:
                    replaceCount += 1
                while replaceCount > k and left <= i:                    
                    if s[left] != c:
                        replaceCount -= 1
                    left += 1
                maxLength = max(maxLength, i - left + 1)

        return maxLength