# LC 1698 (M)
# URL: https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

# Solution
class Solution:
    def countDistinct(self, s: str) -> int:
        
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
                insertions = 0
                for char in word:
                    if not node.contains_char(char):
                        node.put_char(char)
                        insertions += 1
                    node = node.move_to_next_link(char)
                node.set_end()
                return insertions

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
        
        t = Trie()
        distinct = 0
        for i in range(0, len(s)):
            word = s[i:]
            distinct += t.insert(word)
        return distinct
