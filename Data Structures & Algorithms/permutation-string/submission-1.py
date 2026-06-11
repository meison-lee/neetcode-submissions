class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Dict = defaultdict(int)
        s2Dict = defaultdict(int)
        for c in s1:            
            s1Dict[c] += 1                

        for i in range(len(s1)):
                s2Dict[s2[i]] += 1        
                
        for j in range(len(s2) - len(s1)):            
            print(s2Dict)
            if s1Dict == s2Dict:            
                return True

            s2Dict[s2[j]] -= 1
            if s2Dict[s2[j]] == 0:
                del s2Dict[s2[j]]
            s2Dict[s2[j + len(s1)]] += 1            

        return s1Dict == s2Dict