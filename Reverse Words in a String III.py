class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        string = ""
        for i in range(len(s)):
            if i == len(s)-1:
                string+=s[i][::-1]
            else:
                
                string+=s[i][::-1]+" "
            
        return string
        
