# Imp ques
# give number of unique bsts you can make from n nodes

# Link: https://leetcode.com/problems/unique-binary-search-trees/submissions/

# Solution
class Solution:
    def numTrees(self, n: int) -> int:
        
        def get_subtrees(target):
            # Base case
            # No of subtrees with 0 and 1 node is 1
            if target <= 1:
                return 1
            
            val = 0
            for ind in range(0, target):
                left_subtree = get_subtrees(ind)
                right_subtree = get_subtrees(target-ind-1)
                val += (left_subtree * right_subtree)

            return val
        
        return get_subtrees(n)
        
