class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ctr = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    find = nums[i]<nums[j] and nums[j]<nums[k] and nums[j]-nums[i] == diff and nums[k]-nums[j] == diff
                    if find:
                        ctr+=1
        return ctr
