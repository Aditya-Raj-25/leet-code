from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, path):
            if total == target:
                res.append(path[:])
                return
            if i == len(candidates) or total > target:
                return
            dfs(i, total + candidates[i], path + [candidates[i]])
            dfs(i + 1, total, path)

        dfs(0, 0, [])
        return res
