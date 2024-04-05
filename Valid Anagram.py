class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a = s.lower()
        b = t.lower()
        a = "".join(sorted(a))
        b = "".join(sorted(b))
        if a==b:
            return True
        return False
