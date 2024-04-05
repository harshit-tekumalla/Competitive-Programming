class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        high = max(candies)
        for i in candies:
            if i+extraCandies >= high:
                lst.append(i+extraCandies >= high)
            else:
                lst.append(i+extraCandies >= high)
        return lst
        
        
