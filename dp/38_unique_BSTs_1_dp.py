# Link: https://leetcode.com/problems/unique-binary-search-trees/submissions/

class Solution:
    def numTrees(self, n: int) -> int:
        
        def get_subtrees(target, dp):
            # Base case
            # No of subtrees with 0 and 1 node is 1
            if target <= 1:
                return 1
            
            # memo check
            if dp[target] != -1:
                return dp[target]
            
            # recurrence relation
            # for getting the total BSTs
            # Make each node the root
            # all other nodes act as left and right children
            # f(4) = f(0)*f(3) + f(1)*f(2) + f(2)*f(1) + f(3)*f(0) 
            combinations = 0
            for ind in range(0, target):
                left_subtree = get_subtrees(ind, dp)
                right_subtree = get_subtrees(target-ind-1, dp)
                combinations += (left_subtree * right_subtree)
            
            # memoize
            dp[target] = combinations
            return dp[target]
        
        dp = [-1 for _ in range(n+1)]
        return get_subtrees(n, dp)
        
