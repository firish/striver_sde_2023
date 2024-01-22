# great ques
# pretty famous in interviews

# Link: https://leetcode.com/problems/word-ladder/discuss/4609877/Python-simple-brute-force-BFS-solution

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wordList = set(wordList)
        
        q = deque()
        q.append((beginWord, 1)) # (word, transitions)
        while len(q) > 0:
            word, curr_transition = q.popleft()
            
            # Try all characters of current word
            for pos in range(len(word)):
                
                # Try replacing the char with all 26 alphabets
                for ind in range(0, 27, 1):
                    alphabet = chr(ord('a') + ind)
                    new_word = word[:pos] + alphabet + word[pos+1:]
                    
                    if new_word in wordList:
                        if new_word == endWord:
                            return curr_transition+1
                        q.append((new_word, curr_transition+1))
                        wordList.remove(new_word)
        
        return 0
            
        
