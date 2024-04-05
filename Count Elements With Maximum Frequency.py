class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            arr.append(nums.count(i))
        return arr.count(max(arr))
