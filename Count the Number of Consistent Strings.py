class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ctr = 0
        for i in words:
            if set(i).difference(set(allowed)) == set():
                ctr+=1
        return ctr
        
