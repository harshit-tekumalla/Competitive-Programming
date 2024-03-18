class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for rows in matrix:
            if rows[-1]>=target:
                return target in rows
        return False
