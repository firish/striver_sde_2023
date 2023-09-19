# generate valid paranthesis
# works, but TLE


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
