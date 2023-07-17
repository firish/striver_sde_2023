# The famous combination sum problem --variation
# Can use one element only once
# Also, don't give permutations of same combination (only return unique combinations) #IMPORTANT

# Also, can be applicable in irritating problems, 
# where you need the returned arrays/strings answers lexographically sorted 


# Given params
arr = [10, 1, 2, 7, 6, 1, 5]
k = 8
n = len(arr)

def get_unique_combinations(arr, n, ind, target, curr, res):
    # base condition
    if target == 0:
        res.append(curr.copy())
        return
    
    # For this pattern, for every element, 
    # we move from that element to the last element
    for i in range(ind, n, 1):
        # for optimization, use an if check to see if taking the element makes sense
        # since array is sorted, we can break if array element is greater than target
        # as all the next elements will also be bigger
        if arr[i] > target: break

        # Important check
        # For this pattern, we skip calls from similar elements (since we need unique/distinct combinations)
        if (i > ind) and (arr[i] == arr[i-1]): continue  # skip the call

        # Make the recurive call
        curr.append(arr[i])
        get_unique_combinations(arr, n, i+1, target-arr[i], curr, res)
        curr.pop()  # don't forget to clean-up/backtrack

# This is the second main pattern
# For this pattern, we want to sort the array
# Sorting is important, as we can skip same elements while making recursive calls
arr.sort()
res = []
get_unique_combinations(arr, n, 0, k, [], res)
print(res)