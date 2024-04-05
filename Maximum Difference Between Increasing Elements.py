class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i,j = 0,1
        max_diff = 0
        while j<len(nums):
            
            if nums[i]<nums[j]:
                curr_diff = nums[j] - nums[i]
                max_diff = max(curr_diff,max_diff)
                j+=1
            else:
                i = j
                j+=1
        if max_diff == 0:
            return -1
        return max_diff
                
