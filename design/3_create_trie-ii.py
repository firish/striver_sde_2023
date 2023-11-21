# Link: https://leetcode.com/problems/implement-trie-prefix-tree/submissions/

class Node:
    def __init__(self):
        self.data = {}
        self.end = False # denotes end of word

class Trie:

    def __init__(self):
        # every Trie should have a start (root)
        self.root = Node()
        

    def insert(self, word: str) -> None:
        troot = self.root
        for i, char in enumerate(word):
            if char not in troot.data:
                troot.data[char] = Node()
            # after inserting a char
            # or after finding an existing char
            # we go to that char Node
            troot = troot.data[char]
        # when the entire word is over
        # you are at the Node of last char
        # mark its end as true
        troot.end = True
                

    def search(self, word: str) -> bool:
        troot = self.root
        for char in word:
            if char not in troot.data:
                return False
            troot = troot.data[char]
        if troot.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        troot = self.root
        for char in prefix:
            if char not in troot.data:
                return False
            troot = troot.data[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
