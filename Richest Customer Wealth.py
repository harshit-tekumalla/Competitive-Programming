class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst1 = []
        for i in accounts:
            lst1.append(sum(i))
        return max(lst1)
        
