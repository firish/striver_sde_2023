# LC 45 (Medium)
# URL: https://leetcode.com/problems/jump-game-ii/

# Solution: 
class Solution:
    def jump(self, nums: List[int]) -> int:

        def dfs(i, steps):
            if steps >= mini[0]:      # already worse than a known solution
                return
            elif steps >= best[i]:      # can reach i with less steps
                return
            elif i == n-1:
                mini[0] = min(mini[0], steps)
                return
            best[i] = steps
            
            for j in range(nums[i], 0, -1):
                if i + j < n:
                    dfs(i+j, steps+1)
        
        n = len(nums)
        mini = [10**12]
        best = [10**12] * n
        dfs(0, 0)
        return mini[0]
