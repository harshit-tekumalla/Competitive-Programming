import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_n = (n*(n+1))//2
    
        pivot = math.sqrt(sum_n)
       
        if pivot%1==0:
            
            return int(pivot)
        else:
            return -1
