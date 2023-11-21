# Generate all Permutations of an array/string

# using pattern 3 (introducing third pattern)
# Without using a viis/map param
# The way to do this without using a map is to use swapping

# Inputs
arr = [1, 2, 3]
n = len(arr)

# output
res = []

def gen_permuations(arr, n, ind, res):
    # break condition
    if ind >= n:
        res.append(arr.copy())
        return
    
    # for loop
    for i in range(ind, n, 1):
        # swap curr index with right index
        arr[i], arr[ind] = arr[ind], arr[i]
        gen_permuations(arr, n, ind+1, res)
        arr[i], arr[ind] = arr[ind], arr[i] # re-swap and restore the order

gen_permuations(arr, n, 0, res)
print(res)