# Find link at: https://practice.geeksforgeeks.org/problems/median-of-bst/1


def findMedian(root):
    # code here
    # return the median
    nums = []
    def inorder(node, nums):
        if not node: return
        inorder(node.left, nums)
        nums.append(node.data)
        inorder(node.right, nums)
    inorder(root, nums)
    if len(nums) % 2 != 0: 
        return nums[len(nums)//2]
    else: 
        r = nums[len(nums)//2]
        l = nums[(len(nums)//2)-1]
        res = (l+r)/2
        return int(res) if res%1==0 else res

