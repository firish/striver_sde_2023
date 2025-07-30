class BitWiseTrieNode:
  def __init__(self):
      self._links = [None]*2 # 0 and 1
  
  def _get_index(self, char):
      return 0 if char == 0 else 1

  def contains_char(self, bit):
      index = self._get_index(bit)
      return self._links[index] != None
  
  def put_char(self, bit):
      index = self._get_index(bit)
      self._links[index] = BitWiseTrieNode()
  
  def move_to_next_link(self, bit):
      index = self._get_index(bit)
      return self._links[index]


class BitWiseTrie:
    def __init__(self):
        self.root = BitWiseTrieNode()

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

# Initialize bitwise trie
bwt = BitWiseTrie()

# get the max bits needed
hi = max(nums).bit_length() - 1 if nums else 0
bwt.insert(nums[0], hi)
