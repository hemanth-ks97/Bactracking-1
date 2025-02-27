# Time Complexity : O(2^(m+n))
# Space Complexity : O(m+n)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        # 0/1 recursion
        def recurse(i, rem):
            if i == len(candidates) or rem < 0:
                return
            if rem == 0:
                res.append(path[::])
                return
            # don't choose
            recurse(i + 1, rem)
            # choose
            path.append(candidates[i])
            recurse(i, rem - candidates[i])
            # backtrack
            path.pop()
        
        # For loop recursion
        def recurse_loop(pivot, rem):
            if pivot == len(candidates) or rem < 0:
                return
            if rem == 0:
                res.append(path[::])
                return
            
            for i in range(pivot, len(candidates)):
                path.append(candidates[i])
                recurse_loop(i, rem - candidates[i])
                path.pop()
        
        recurse_loop(0, target)

        return res