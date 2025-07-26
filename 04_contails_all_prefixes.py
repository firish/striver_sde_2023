# LC 720 and LC 1858 (Medium)
# URL:

# Naive Solution
from collections import defaultdict
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # URL: https://leetcode.com/problems/implement-trie-prefix-tree/

        class TrieNode:
            def __init__(self):
                self._links = [None]*26
                self._is_end = False
            
            def _get_index(self, char):
                return ord(char) - ord('a')

            def contains_char(self, char):
                index = self._get_index(char)
                return self._links[index] != None
            
            def put_char(self, char):
                index = self._get_index(char)
                self._links[index] = TrieNode()
            
            def move_to_next_link(self, char):
                index = self._get_index(char)
                return self._links[index]

            def set_end(self):
                self._is_end = True
            
            def check_end(self):
                return self._is_end


        class Trie:

            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str) -> None:
                node = self.root
                for char in word:
                    if not node.contains_char(char):
                        node.put_char(char)
                    node = node.move_to_next_link(char)
                node.set_end()

            def search(self, word: str) -> bool:
                node = self.root
                for char in word:
                    if not node.contains_char(char):
                        return False
                    node = node.move_to_next_link(char)
                return node.check_end()

            def startsWith(self, prefix: str) -> bool:
                node = self.root
                for char in prefix:
                    if not node.contains_char(char):
                        return False
                    node = node.move_to_next_link(char)
                return True

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = defaultdict(list)
        maxi = 0
        for word in words:
            if len(word) < maxi:
                continue

            all_prefixes_found = True
            for ind in range(len(word)):
                prefix = word[:ind+1]
                if not trie.search(prefix):
                    all_prefixes_found = False
                    break
            if all_prefixes_found:
                maxi = len(word)
                res[maxi].append(word)
                
        candidate_words = res[maxi]
        if len(candidate_words) == 0:
            return ""
        elif len(candidate_words) == 1:
            return candidate_words[0]
        else:
            return sorted(candidate_words)[0]



# More effecient solution that walks the trie just N times instead of N*L times
from collections import defaultdict
class Solution:
    def longestWord(self, words: List[str]) -> str:

        class TrieNode:
            def __init__(self):
                self._links = [None]*26
                self._is_end = False
            
            def _get_index(self, char):
                return ord(char) - ord('a')

            def contains_char(self, char):
                index = self._get_index(char)
                return self._links[index] != None
            
            def put_char(self, char):
                index = self._get_index(char)
                self._links[index] = TrieNode()
            
            def move_to_next_link(self, char):
                index = self._get_index(char)
                return self._links[index]

            def set_end(self):
                self._is_end = True
            
            def check_end(self):
                return self._is_end


        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str) -> None:
                node = self.root
                for char in word:
                    if not node.contains_char(char):
                        node.put_char(char)
                    node = node.move_to_next_link(char)
                node.set_end()

            def search(self, word: str) -> bool:
                node = self.root
                for char in word:
                    if not node.contains_char(char):
                        return False
                    node = node.move_to_next_link(char)
                return node.check_end()

            def startsWith(self, prefix: str) -> bool:
                node = self.root
                for char in prefix:
                    if not node.contains_char(char):
                        return False
                    node = node.move_to_next_link(char)
                return True
            
            def includesAllPrefixes(self, word: str) -> bool:
                node = self.root
                for char in word:
                    if not node.contains_char(char):
                        return False
                    node = node.move_to_next_link(char)
                    if not node.check_end():
                        return False
                return True

        # soln
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = defaultdict(list)
        maxi = 0
        for word in words:
            if len(word) < maxi:
                continue

            if trie.includesAllPrefixes(word):
                maxi = len(word)
                res[maxi].append(word)
                
        candidate_words = res[maxi]
        if len(candidate_words) == 0:
            return ""
        elif len(candidate_words) == 1:
            return candidate_words[0]
        else:
            return sorted(candidate_words)[0]
                
