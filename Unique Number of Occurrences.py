class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr1 = list(set(arr))
        count_c = []
        for i in arr1:
            occ = arr.count(i)
            count_c.append(occ)
        if len(list(set(count_c))) == len(arr1):
            return True
        else:
            return False
            
