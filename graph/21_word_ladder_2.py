# link: https://leetcode.com/problems/word-ladder-ii/submissions/

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        n = len(beginWord)
        wordList = set(wordList)
        shortest = [10**10]
        first = False
        
        def word_ladder(curr_word, curr_transitions, ind, curr_ladder, res):
            # if ind >= n:
            # print('here ', curr_word, curr_ladder)
            if curr_word == endWord:
                shortest[0] = min(shortest[0], len(curr_ladder))
                res.append(curr_ladder.copy())
                return
            
            # Try all characters of current word
            for pos in range(0, len(curr_word)):
                
                # Try replacing the char with all 26 alphabets
                for i in range(0, 27, 1):
                    alphabet = chr(ord('a') + i)
                    new_word = curr_word[:pos] + alphabet + curr_word[pos+1:]
                    
                    if new_word in wordList:
                        wordList.remove(new_word)
                        word_ladder(new_word, curr_transitions+1, i, curr_ladder + [new_word], res)
                        wordList.add(new_word)
        
        res = []
        word_ladder(beginWord, 1, 0, [beginWord], res)
        ans = []
        for seq in res:
            if len(seq) == shortest[0]:
                ans.append(seq)
        return ans
