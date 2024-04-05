class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lst1 = []
        
        for i in sentences:
            ctr = 0
            lst = list(i)
            for j in range(len(lst)):
                if lst[j] == " ":
                    ctr+=1
                if j == len(lst)-1:
                    ctr+=1 
            lst1.append(ctr)
        return max(lst1)
        
