class TrieNode:
    def __init__(self):
        self._links = [None] * 26
        self._is_end = False

    def _idx(self, ch):                        # helper: a → 0 … z → 25
        return ord(ch) - ord('a')

    def contains(self, ch):
        return self._links[self._idx(ch)] is not None

    def put(self, ch):
        self._links[self._idx(ch)] = TrieNode()

    def next(self, ch):
        return self._links[self._idx(ch)]

    def set_end(self):     
      self._is_end = True
    def is_end(self):      
      return self._is_end

    def has_no_children(self):
        return all(link is None for link in self._links)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch)
            node = node.next(ch)
        node.set_end()

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.contains(ch):
                return False
            node = node.next(ch)
        return node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.contains(ch):
                return False
            node = node.next(ch)
        return True


    # The idea
    # To erase a word you walk down the same path you followed when you inserted it.
    # Once you reach the last character you unset the _is_end flag.
    # Then, as recursion unwinds, you prune any node that:
      # has no children left, and
      # is not the end of another word.

    def delete(self, word: str) -> bool:
        return self._delete(self.root, word, 0)

    def _delete(self, node: TrieNode, word: str, depth: int) -> bool:
        if node is None:
            return False                            # safety check

        # end condition
        if depth == len(word):                      # end of word
            if not node.is_end():
                return False                        # word wasn’t stored
            node._is_end = False                    # un‑mark
            return node.has_no_children()           # prune if empty

        ch = word[depth]
        child = node.next(ch)
        # recurse
        if not self._delete(child, word, depth + 1):
            return False                            # nothing will be pruned above

        # pruning
        # child can be safely removed
        node._links[node._idx(ch)] = None
        # decide if *current* node can be pruned
        return (not node.is_end()) and node.has_no_children()
