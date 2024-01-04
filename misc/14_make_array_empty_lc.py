# Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from collections import defaultdict, Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x = Counter(nums)
        
		res = 0
        for num, cnt in x.items():
            if cnt >= 3:
                res += cnt // 3
                if cnt % 3 != 0:
                    res += 1
            elif cnt >= 2:
                res += cnt // 2
                if cnt % 2 != 0:
                    res += 1
            else:
                return -1
        
		return res
