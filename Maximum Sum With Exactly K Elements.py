class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_lst = []
        for i in range(k):
            k = max(nums)
            max_lst.append(k)
            nums.append(k+1)
            nums.pop(nums.index(k))
            
        return sum(max_lst)
            
        
