# LC 3152
# Special Array 2
# Pefix Sum 

# ques url: https://leetcode.com/problems/special-array-ii/

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        # Construct diff array
        diff = [0]*(n-1)
        for i in range(n-1):
            if (nums[i] % 2) != (nums[i+1] % 2):
                diff[i] = 1
        
        # Prefix sum of diff
        pdiff = [0]*(n-1)
        if n > 1:
            pdiff[0] = diff[0]
        for i in range(1, n-1):
            pdiff[i] = pdiff[i-1] + diff[i]
        
        res = []
        for start, end in queries:
            # if start and end ind is the same, it's always special
            if start == end:
                res.append(True)
                continue
            
            # pairs in range
            total_pairs = end - start
            
            # count of parity switches in range
            count_at_end = pdiff[end-1]
            count_at_start = pdiff[start-1] if start > 0 else 0
            pair_diff_count =  count_at_end - count_at_start
            
            res.append(pair_diff_count == total_pairs)
            
        return res
