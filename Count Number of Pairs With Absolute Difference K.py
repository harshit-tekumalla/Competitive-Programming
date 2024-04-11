class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ctr = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j] and abs(nums[i] - nums[j]) == k:
                    ctr+=1
        return ctr
