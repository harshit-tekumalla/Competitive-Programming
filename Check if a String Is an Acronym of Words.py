class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        string = ""
        for i in words:
            string+=i[0]
        if string == s:
            return True
        return False
