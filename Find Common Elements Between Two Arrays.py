class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        ctr = 0
        for i in nums1:
            if nums2.count(i)>=1:
                ctr+=1
        output.append(ctr)
        ctr = 0
        for i in nums2:
            if nums1.count(i)>=1:
                ctr+=1
        output.append(ctr)
        return output
                
        
