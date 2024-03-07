# Link: https://leetcode.com/problems/edit-distance/discuss/4836582/Python-using-simple-dp

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def lavensthein(w1, w2, memo):
            # base case
            if w1 < 0:
                return w2
            if w2 < 0:
                return w1
            
            # memo check
            if (w1, w2) in memo:
                return memo[(w1, w2)]
            
            # allowed operations
            add = lavensthein(w1-1, w2, memo) + 1
            delete = lavensthein(w1, w2-1, memo) + 1
            
            cost = 0 if word1[w1] == word2[w2] else 1
            update = lavensthein(w1-1, w2-1, memo) + cost
                
            # update memo
            memo[(w1, w2)] = min(add, delete, update)
            return memo[(w1, w2)]
        
        memo = {}
        return lavensthein(len(word1)-1, len(word2)-1, memo) + 1
