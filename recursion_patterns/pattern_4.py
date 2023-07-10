# Pattern 4

# printing subsequences that have some K
# BUT ONLY FIND THE COUNT

# Follows the same pattern, 
# Take the element, or skip it.

# structure 
# base condition - return 0 or 1
# l = func()
# r = func()
# return l + r

# Additional optimization
# you no longer need the res data structure 
# as you are not printing anything


def find_subseq_with_sum_k(arr, ind, total, k):
    # stop condition
    if ind >= n:
        if total == k:
            return 1
        return 0
    
    # condition 1, take the element
    total += arr[ind]
    take = find_subseq_with_sum_k(arr, ind+1, total, k)

    # condition 2, skip the element
    total -= arr[ind]
    skip = find_subseq_with_sum_k(arr, ind+1, total, k)
    
    # if both the cases don't return True, return False
    return take + skip


k = 9
arr = [1, 2, 3, 4, 5]
n = len(arr)

# driver 
count = find_subseq_with_sum_k(arr, 0, 0, k)
print(count)