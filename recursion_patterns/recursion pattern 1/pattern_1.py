# Recursion pattern 1
# Subsequenc problems
# push and pop off the recursion stack
# A simplified version of backtracking.

# This pattern works on the principle of choice
# For each element you have two choices
# you can take it or not take it (1 or 0)

# Problem to recursively print all subsequences of an array/string

arr = [1, 2, 3, 4]
n = len(arr)

def print_subsequences(arr, n, ind, res):
    if ind == n:
        print(res)
        return 
    
    # choice 1, take the element
    res.append(arr[ind])
    print_subsequences(arr, n, ind+1, res)

    # choice 2, skip the element
    res.pop() # backtrack..
    print_subsequences(arr, n, ind+1, res)


print_subsequences(arr, n, 0, [])