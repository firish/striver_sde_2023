# Designing a dictionary

# Dict is nothing but a key-value pair. {"apple": 5}
# Dict is used for O(1) lookup in a runtine.

# Dict is also used in programming language's runtime. 
# This is done in symbolic tables. If you have variables, or functions
# The memory location of these variables, function, program routines is stored in a table called symbolic table
# This table is nothing but a key-value store, or a dictionary.

# Next, it is important to note that we can only store immutable data-types as dictionary keys, like int, str, or tuple
# mutable data types like lists are not allowed. 


# The basic working of a dict. (IMP)
# Dictionaries are nothing but a class that uses the array data structure smartly.
# Dictionaries work with a double hashing system.
# the first hash converts str, int, tuple -> f() -> to a large int values
# Example, "Apple" -> f1() -> 12789902
# But if hash values are so big, the size of the bin array will be very huge
# This is pure of wastage of space
# So we have a second hash function, that converts the large ints into
# small ints within a range of [0, M]. The value of m is different for different languages
# Next there is an array of size M,
# If we have a key "apple" and val 5 -> f1(apple) -> 12789902 -> f2(12789902) -> 12 then we store bin[12] = 5
# The second hash function is typically something simple like 12789902 % M, to make 12789902 fit in [0, M]
# next we can do bin[12] and get 5 in O(1) look-up time. 


# But, what happens  when you have stored M keys, and need to store more keys? 
# The hash table has a load_factor
#  The load factor is the ratio of the number of items in the hash table to the total number of slots/buckets available. 
# whenever the load_factor exceeds a threshold, the M (size of bin array) is changed
# different languages change the size by a different value, but a popular approach is to double the M
# Note, when this happens, the hash function f2() changes
# hence all the keys in the bin array need to be assigned to a new index based on the new hashing
# So this is a very costly operation.

# What happens when multiple keys 
# key1 -> f1() -> f2 -> i
# key2 -> f1() -> f2 -> i
# key2 -> f1() -> f2 -> i
# all map to the same index?
# This is called a collision
# If we do not handle collisions the data at that index will be overwritten
# This makes the dictionary a lossy data structure
# To avoid this, there are two classic methods employed,
# 1) Chaining,
# 2) Open-Indexing (used by modern languages like Python and Go)


# 1) Chaining
# base idea: if multiple keys hash to the same value, store all of them
# a typical data structure for this is a linked-list
# every index can be a head, and when another key hashes to that index
# we create another node and link it to the previously existing node for that index
# this creates a kind of chain "chaining" (multiple keys chained to an index)
# so chaining-based dict is nothing but an array where element is a linked-list

# languages where we can dynamically change the size of data structures, e.g Python
# can simplify this implementation using an array of arrays

# one problem with this approach,
# when collisions occur, we create a chain
# adding nodes is O(1), but deleting and look-up require traversal and are O(k), 
# where k is the number of collisions for that index
# and if we use an array instead of linked list, then lookup and deletion both become O(k)

# to make this more effective,
# you can maintain a self-balancing binary tree
# so dictionary becomes an array, where each index is the root of a self-balancing tree
# this makes lookup O(log.k), 
# however, this also makes the insertions and deletions O(log.k)
# so there exists a trade-off. 



# 2) Open Addressing, or Open Indexing
# basic idea:  when we have a collision, try to find another empty index for this key
# however, this new index can't be random, we have to find it "deterministically"
# a method to do this is by using "probing"

# to do this we use a probing function
# the function should be deterministic and cover the entire range [0, M]
# for every key we call the prob(key, 0), here 0, is the 0th attempt
# if there is a collision and a value already exists at that index, we call prob(key, 1)
# in the worst case, we have to make M calls
# since func is deterministic in nature, for the same key "k1" the prob() will always generate the indexes to check in the same order

# example
# say prob(key1, 0) -> 5
# prob(key2, 0) -> 5, so prob(key2, 1) -> 2
# prob(key3, 0) -> 5, so prob(key3, 1) -> 2, prob(key3, 2) -> 3
# insertions and lookups are in open addressing are regular
# if you look up k2, prob(key2, 0) -> 5, you don't find key2 at 5
# so you do prob(key2, 1) -> 2, and find k2
# avg case, insertion and look-up both will be O(k),

# All deletes in open addressing are soft deletes
# if you do a regular (hard) delete, say key1
# you will empty that index, so ind 5 will be empty
# now if you try to get key2
# prob(key2, 0) -> 5, but 5 is empty, so you would think that dict does not have k2
# hence we need to diffrentiate between empty and deleted slot
# hence we use soft delete, simplest way to do so is put -1 for delted index vals

# advantage is that we don't use an auxilary storage like Linkedlist or balanced binary tree like chaining, saving space and complexity of operation
# disadvantage is that max number of keys = M, while in chaining, you can have unlimited keys

# The efficiency of the open addressing is dependent upon the probing function
# there are three common types of probing functions

# A) Linear Probing



# Here is a basic dictionary class implementation in Python
class Dict:
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def check_load_factor_and_resize(self):
        # Grow the table
        if self.count > 0.67 * self.size:
            self.resize(self.size * 2)
        # Shrink the table
        elif self.count < 0.125 * self.size and self.size > 10:
            self.resize(self.size // 2)

    def insert(self, key, value):
        self.check_load_factor_and_resize()
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Insert new key
        self.count += 1

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                del bucket[i]  # Delete the key-value pair
                self.count -= 1
                self.check_load_factor_and_resize()
                return True
        return False  # Return False if the key was not found

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for kv in bucket:
            if kv[0] == key:
                return kv[1]
        raise KeyError(f"Key not found: {key}")

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        if not self.delete(key):
            raise KeyError(f"Key not found: {key}")

    def __repr__(self):
        return '{' + ', '.join(f'{k}: {v}' for bucket in self.table for k, v in bucket) + '}'

