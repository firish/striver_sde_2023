# Subset sums
# Calculate sum of all subsets of the array
# Return the sums in ascending order 

from collections import defaultdict
import heapq

# Given params
arr = [1, 8, 3, 3]
n = len(arr)

# define output
res = []
stored = defaultdict(bool)
# convert res to a heap so that you can insert in a sorted manner in constant order time
heapq.heapify(res)


def subset_sums(arr, n, ind, curr, res):
    # break condition
    if ind == n:
        if curr not in stored:
            heapq.heappush(res, curr)
            stored[curr] = True
        return
    
    # cond 1, take the element
    curr += arr[ind]
    subset_sums(arr, n, ind+1, curr, res)
    
    # cond 2, skip the element
    curr -= arr[ind]
    subset_sums(arr, n, ind+1, curr, res)


subset_sums(arr, n, 0, 0, res)
while res: print(heapq.heappop(res), end=' ')

# This approach uses a heap and a hashmap to avoid sorting
# Will be beneficial is input arr has a lot of elements, otherwise, sorting is simpler and almost as effective.