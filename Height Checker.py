class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ctr = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                ctr+=1
        return ctr
        
