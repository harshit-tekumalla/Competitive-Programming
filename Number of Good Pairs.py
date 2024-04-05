class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # j = 1
        # for i in range(len(nums)):
        #     if nums[i] == nums[j]:
        #         ctr+=1
        #         j+=1
        #     else:
        #         j+=1
        ctr = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    ctr+=1
                
        return ctr
                    
                    
        
