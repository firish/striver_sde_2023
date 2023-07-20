# Pattern 2

# printing subsequences that have some K
# BUT ONLY PRINT 1

# Follows the same pattern, 
# Take the element, or skip it.


def find_subseq_with_sum_k(arr, ind, res, total, k):
    # stop condition
    if ind >= n:
        if total == k:
            print(res)
            return True
        return False
    
    # condition 1, take the element
    total += arr[ind]
    res.append(arr[ind])
    if(find_subseq_with_sum_k(arr, ind+1, res, total, k)):
        return True

    # condition 2, skip the element
    total -= arr[ind]
    res.pop()
    if(find_subseq_with_sum_k(arr, ind+1, res, total, k)):
        return True
    
    # if both the cases don't return True, return False
    return False


k = 9
arr = [1, 2, 3, 4, 5]
n = len(arr)
find_subseq_with_sum_k(arr, 0, [], 0, k)