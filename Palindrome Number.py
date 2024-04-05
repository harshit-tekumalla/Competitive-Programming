class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        lst = []
        for i in y:
            lst.append(i)
        
        
        lst1 = lst[::-1]
        if lst == lst1:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
