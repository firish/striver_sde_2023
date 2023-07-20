# A combination sum type proble
# get all combinations that make up a sum
# plus, REPEATING elements is allowed.

# given
arr = [ 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 12

n = len(arr) 
res = []

def get_sum_combinations(arr, n, ind, target, curr, res):
    # base case
    if ind == n:
        if target == 0:
            # Remember, to append an copy, as when curr changes, 
            # your results stored in res will also change
            res.append(curr.copy())
        return
    
    # case 1, we take the element (multiple times)
    # but check, if it is valid first
    if arr[ind] <= target:
        target -= arr[ind]
        curr.append(arr[ind])
        get_sum_combinations(arr, n, ind, target, curr, res)
        # before taking the next element, clean up
        curr.pop()
        target += arr[ind]
    
    # case 2, we do not take this element any more
    get_sum_combinations(arr, n, ind+1, target, curr, res)

get_sum_combinations(arr, n, 0, k, [], res)
print(res)