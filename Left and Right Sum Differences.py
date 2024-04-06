class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        answer = []
        for i in range(len(nums)):
            leftSum.append(sum(nums[0:i]))
            rightSum.append(sum(nums[i+1:]))
        for i in range(len(leftSum)):
            answer.append(abs(leftSum[i] - rightSum[i]))
        return answer
            
                
            
            
            
        
