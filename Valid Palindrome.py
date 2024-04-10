class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(s)
        string  = string.lower()
        string1 = ""
        for i in string:
            if i.isalnum():
                string1+=i
        lst = list(string1)
        if lst[::-1] == lst:
            return True
        else:
            return False
