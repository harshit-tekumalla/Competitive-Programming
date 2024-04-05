class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # lst = nums[0:n]
        # lst1 = nums[n:]
        # lst3 = []
        # for i in range(len(lst)):
        #     lst3.append(lst[i])
        #     for j in range(len(lst1)):
        #         lst3.append(lst1[j])
        #         lst1.pop(j)
        #         break
        # return lst3
        lst1 = []
        lst2 = []
        lst3 = []
        for i in range(n):
            lst1.append(nums[i])
        for i in range(n,n*2):
            lst2.append(nums[i])
        for i in range(n):
            lst3.append(lst1[i])
            lst3.append(lst2[i])
        return lst3
        
            
        
        
