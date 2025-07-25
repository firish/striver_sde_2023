# URL: https://leetcode.com/problems/implement-trie-ii-prefix-tree/

# MY SOLN
class TrieNode:
    def __init__(self):
        self._links = [None]*26
        self._end_count = 0
        self._prefix_count = 0
    
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

    def increment_word_count(self):
        self._end_count += 1
    
    def increment_prefix_count(self):
        self._prefix_count += 1
    
    def get_word_count(self):
        return self._end_count
    
    def get_prefix_count(self):
        return self._prefix_count
    
    def decrement_word_count(self):
        if self._end_count >= 1:
            self._end_count -= 1
    
    def decrement_prefix_count(self):
        if self._prefix_count >= 1:
            self._prefix_count -= 1


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ind, char in enumerate(word):
            # if the char doesn't exist, add it as a new TrieNode
            if not node.contains_char(char):
                node.put_char(char)
            # move to the next TrieNode
            node = node.move_to_next_link(char)
            # increase prefix count, as one more word with the current prefix search exists
            node.increment_prefix_count()
        # increase prefix count, as one more word with the current prefix search exists
        node.increment_word_count()
        

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            # if the combination doesnt exist, return 0
            if not node.contains_char(char):
                return 0
            # traverse the trie
            node = node.move_to_next_link(char)
        # return the number of occurances of the target word
        return node.get_word_count()

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            # if the combination doesnt exist, return 0
            if not node.contains_char(char):
                return 0
            # traverse the trie
            node = node.move_to_next_link(char)
        # return the number of occurances of the prefix word
        return node.get_prefix_count()
        
    def erase(self, word: str) -> None:
        node = self.root
        for char in word:
            # if the combination doesnt exist, return
            if not node.contains_char(char):
                return
            # if it exists, traverse the trie
            node = node.move_to_next_link(char)
            # reduce the prefix count by 1
            node.decrement_prefix_count()
        # if entire word is found, reduce the word count by 1
        node.decrement_word_count()
        return


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
