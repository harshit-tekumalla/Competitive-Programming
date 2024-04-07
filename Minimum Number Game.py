class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # alice_min = 0
        # bob_min = 0
        # arr = []
        # for i in range(len(nums)):
        #     if nums[i] == min(nums):
        #         alice_min+=nums[i]
        #         nums.pop(i)
        #         bob_min+=min(nums)
        #         nums.pop(nums.index(bob_min))
        #         arr.append(bob_min)
        #         arr.append(alice_min)
        #         alice_min = 0
        #         bob_min = 0
        res=[]
        nums=sorted(nums)
        for i in range(0,len(nums),2):
            res.extend(nums[i:i+2][::-1])
        return res
                
        
                    
                
        
