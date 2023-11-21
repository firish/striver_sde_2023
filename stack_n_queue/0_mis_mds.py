arr = [1, 7, 4, 3, 5, 6, 9, 2, 6, 11, 15, 14, 12, 13, 3, 20]
print(arr)

# For the next greater element: 
# Use a Monotonically Increasing Stack (MIS) and 
# traverse from right to left.
n = len(arr)
mis = []
next_greater = [-1]*n
for i, num in enumerate(arr[::-1]):
    ind = n-i-1
    # if stack has elements, pop until the top of stack has next greater
    while len(mis) > 0 and num > mis[-1]:
        mis.pop()
    
    # after poping, if stack still has elements, next greater element exists
    if len(mis) > 0:
        next_greater[ind] = mis[-1]
    
    # at the end, always add current element to top of stack
    mis.append(num)
print(next_greater)


# For the next smaller element: 
# Use a Monotonically Decreasing Stack (MDS) and 
# traverse from right to left.
n = len(arr)
mds = []
next_smaller = [-1]*n
for i, num in enumerate(arr[::-1]):
    ind = n-i-1
    # if stack has elements, pop until the top of stack has next smaller
    while len(mds) > 0 and num < mds[-1]:
        mds.pop()
    
    # after poping, if stack still has elements, next greater element exists
    if len(mds) > 0:
        next_smaller[ind] = mds[-1]
    
    # at the end, always add current element to top of stack
    mds.append(num)
print(next_smaller)