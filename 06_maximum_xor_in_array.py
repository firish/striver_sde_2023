# LC 421 (Medium)
# URL: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/?envType=problem-list-v2&envId=trie


# Solution
# Has a **binary variant** of the trie

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        class TrieNode:
            def __init__(self):
                self._links = [None]*2 # 0 and 1
            
            def _get_index(self, char):
                return 0 if char == 0 else 1

            def contains_char(self, bit):
                index = self._get_index(bit)
                return self._links[index] != None
            
            def put_char(self, bit):
                index = self._get_index(bit)
                self._links[index] = TrieNode()
            
            def move_to_next_link(self, bit):
                index = self._get_index(bit)
                return self._links[index]


        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, num, hi):
                node = self.root
                for bit_ind in range(hi, -1, -1):
                    bit = (num >> bit_ind) & 1 # gets 1 or 0
                    if not node.contains_char(bit):
                        node.put_char(bit)
                    node = node.move_to_next_link(bit)
            
            def get_maximum_xor(self, num, hi):
                res = 0
                node = self.root
                for bit_ind in range(hi, -1, -1):
                    bit = (num >> bit_ind) & 1
                    target = 1 if bit == 0 else 0
                    if node.contains_char(target):
                        res = res | (1 << bit_ind)
                        node = node.move_to_next_link(target)
                    else:
                        node = node.move_to_next_link(bit)
                return res
        
        # get the max bits needed
        hi = max(nums).bit_length() - 1 if nums else 0

        t = Trie()
        # seed the trie with first number
        t.insert(nums[0], hi)

        # get the xor of next number with the trie and then add the number
        maxi = 0
        for num in nums[1:]:
            # get the maximum xor value possible
            res = t.get_maximum_xor(num, hi)
            maxi = max(maxi, res)
            # insert the number
            t.insert(num, hi)

        return maxi
