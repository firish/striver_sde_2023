# Power set
# same as generating all subsets/subsequences
# However, a power set does not have duplicates

# So, we need only unique subsets
# Therefore, pattern 2 is more suitable for generating a power set

# Inputs
arr = [1, 2, 2, 3, 3, 3]
n = len(arr)

# Output
res = []


def power_set(arr, n, ind, curr, res):
    res.append(curr.copy())
    
    # for loop, for first to last element
    for i in range(ind, n, 1):
        # condition for avoiding duplicates
        if i > ind and arr[i] == arr[i-1]: continue

        # take everything else
        curr.append(arr[i])
        power_set(arr, n, i+1, curr, res)
        curr.pop()


# driver code
arr.sort() # required with this recursion pattern
power_set(arr, n, 0, [], res)
print(res)