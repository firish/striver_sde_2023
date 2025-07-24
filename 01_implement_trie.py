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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
