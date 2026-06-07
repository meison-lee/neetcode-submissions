class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0;
        while (i < len(s)):
            while (s[j] != "#"):
                j += 1;
            num = int(s[i:j])
            i = j + 1
            res.append(s[i:i + num])
            i += num
            j = i
        return res