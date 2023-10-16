# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.data = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        troot = self.root
        for char in word:
            if char not in troot.data:
                troot.data[char] = Node()
            troot = troot.data[char]
        troot.end = True

    def search(self, word: str) -> bool:
        
        def dfs(ind, troot):
            if ind == len(word):
                return troot.end
            
            if word[ind] != '.':
                if word[ind] in troot.data:
                    return dfs(ind+1, troot.data[word[ind]])
                else:
                    return False
            else:
                # wildcard character
                for char, data in troot.data.items():
                    flag = dfs(ind+1, troot.data[char])
                    if flag:
                        return True
                return False
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
