class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        nums.sort()
        while l<=r:
            if -nums[l]==nums[r]:
                return nums[r]
            elif -nums[l]>nums[r]:
                l+=1
            else:
                r-=1
        return -1
        
