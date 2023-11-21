# generate valid paranthesis
# works, but TLE
# Link: https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # get the base array
        arr = ['(']*n + [')']*n
        # now the question becomes -> get all permutations of this array
        # add logic to keep only valid combinations
        def gen(arr, curr, freq, n, res):
            # validity condition
            if freq['('] > n or freq[')'] > n:
                return
            elif freq['('] < freq[')']:
                return
            # break conditions
            if len(curr) == len(arr):
                res.append(''.join(curr))
                return
        
            # loop through the array
            # try every array element at each index of curr
            # keep a track of freq to keep valid permutations
            for ind in range(0, len(arr), 1):
                curr.append(arr[ind])
                freq[arr[ind]] += 1
                gen(arr, curr, freq, n, res)

                # backtrack
                freq[curr.pop()] -= 1
            
        freq = {'(':0, ')': 0}
        res = []
        gen(arr, [], freq, n, res)
        return set(res)


# Did not require the for loop pattern, simply use take not take with freq condition
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def gen(curr, open_count, close_count):
            # if the current combination is valid, add to the result
            if curr and len(curr) == 2 * n:
                res.append(''.join(curr))
                return
            
            # If we can add an opening parenthesis, do it
            if open_count < n:
                curr.append('(')
                gen(curr, open_count + 1, close_count)
                curr.pop()
            
            # If we can add a closing parenthesis, do it
            if close_count < open_count:
                curr.append(')')
                gen(curr, open_count, close_count + 1)
                curr.pop()
        
        res = []
        curr = []
        gen(curr, 0, 0)
        return res
