class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        e = {}
        for ch in s:
            d[ch] = d.get(ch,0) + 1
        for ch in t:
            e[ch] = e.get(ch,0) + 1
        return d == e


