class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d ={}
        for i in range(len(paths)):
            d[paths[i][0]] = paths[i][1]
        for i in d.values():
            if i not in d.keys():
                return i
                break
        
