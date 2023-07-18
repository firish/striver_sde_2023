# Generate all Permutations of an array/string

# using pattern 3 (introducing third pattern)
# uses an additional recursion param -> vis
# vis basically points to the indices that are still available to use

# Inputs
arr = [1, 2, 3]
n = len(arr)

# output
res = []
vis = [0]*n

def gen_permuations(arr, n, ind, curr, vis, res):
    # break condition
    if len(curr) == n:
        res.append(curr.copy())
        return
    
    # for loop
    for i in range(0, n, 1):
        # if you are yet to take the element on this index
        if vis[i] == 0:
            vis[i] = 1 # mark as taken
            curr.append(arr[i]) # take element
            gen_permuations(arr, n, i+1, curr, vis, res)
            # clean up after coming back (backtrack)
            curr.pop()
            vis[i] = 0

gen_permuations(arr, n, 0, [], vis, res)
print(res)