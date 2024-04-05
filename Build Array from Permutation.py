class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            a = nums[nums[i]]
            ans.append(a)
        return ans
            
