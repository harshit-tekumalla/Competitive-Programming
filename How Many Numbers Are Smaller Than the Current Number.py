class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # lst = []
        # ctr = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] < nums[j]:
        #             ctr += 1
        #     lst.append(ctr)
        #     ctr = 0
        cnt = 0
        lst = []
        for i in nums:
            for j in nums:
                if i!=j and j<i:
                    cnt+=1
            lst.append(cnt)
            cnt = 0
        return lst
            
        

                
