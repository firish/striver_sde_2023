# Pattern 2

# printing subsequences that have some K

# Follows the same pattern, 
# Take the element, or skip it.

def find_subseq_with_sum_k(arr, ind, res, total, k):
    # stop condition
    if ind >= n:
        if total == k:
            print(res)
        return
    
    # condition 1, take the element
    total += arr[ind]
    res.append(arr[ind])
    find_subseq_with_sum_k(arr, ind+1, res, total, k)

    # condition 2, skip the element
    total -= arr[ind]
    res.pop()
    find_subseq_with_sum_k(arr, ind+1, res, total, k)


k = 9
arr = [1, 2, 3, 4, 5]
n = len(arr)
find_subseq_with_sum_k(arr, 0, [], 0, k)