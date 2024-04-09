class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # string = ""
        # for i in words:
        #     if list(i[::-1]) == list(i):
        #         for j in i:
        #             string+=j
        #         break
        # return string
        for i in words:
            if i[::-1] == i:
                return i
                break
        return ""
        
