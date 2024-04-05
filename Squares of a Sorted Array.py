class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst1=[]
        for i in nums:
            lst1.append(i*i)
            lst1 = sorted(lst1)
        return lst1
        
