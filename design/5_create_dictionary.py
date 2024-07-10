# Designing a dictionary

####################################################### Introduction #######################################################
# What is a dict?
# Dict is nothing but a key-value pair. {"apple": 5}
# Dict is used for O(1) lookup in a runtine.
# Next, it is important to note that we can only store immutable data-types as dictionary keys, like int, str, or tuple
# mutable data types like lists are not allowed. 

# An interesting use case of dictionaries!
# Dict is also used in programming language's runtime. 
# This is done in symbolic tables. If you have variables, or functions
# The memory location of these variables, function, program routines is stored in a table called symbolic table
# This table is nothing but a key-value store, or a dictionary.


####################################################### Basic Working #######################################################
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


####################################################### Dynamic Sizing #######################################################
# But, what happens  when you have stored M keys, and need to store more keys? 
# The hash table has a load_factor
#  The load factor is the ratio of the number of items in the hash table to the total number of slots/buckets available. 
# whenever the load_factor exceeds a threshold, the M (size of bin array) is changed
# different languages change the size by a different value, but a popular approach is to double the M
# Note, when this happens, the hash function f2() changes
# hence all the keys in the bin array need to be assigned to a new index based on the new hashing
# So this is a very costly operation.


################################################# Hashing Conflict #######################################################
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


################################################# Conflicts: CHAINING  ###############################################
# base idea: if multiple keys hash to the same value, store all of them
# a typical data structure for this is a linked-list.
# every index can be a head, and when another key hashes to that index
# we create another node and link it to the previously existing node for that index
# this creates a kind of chain "chaining" (multiple keys chained to an index)
# so chaining-based dict is nothing but an array where every element is a linked-list head node

# IMP NOTE:
# languages where we can dynamically change the size of data structures, e.g Python, Java (Dynamic Vectors)
# can simplify this implementation using an array of arrays

# one problem with this approach,
# when collisions occur, we create a chain
# adding nodes is O(1), but deleting and look-up require traversal and are O(k), 
# where k is the number of collisions for that index (or, simply, the length of that chain)
# and if we use an array instead of linked list, then insertion, lookup, and deletion, all become O(k)

# to make this more effective,
# you can maintain a "self-balancing binary tree"
# so dictionary becomes an array, where each index is the root of a self-balancing tree
# this makes lookup and deletions O(log.k), 
# however, this also makes the insertions O(log.k)
# so there still exists a trade-off. 


########################################## Conflicts: OPEN ADDRESSING ###############################################
# basic idea:  when we have a collision, try to find another empty index for this key
# however, this new index can't be random, we have to find it "deterministically"
# a method to do this is by using "probing"

# to do this we use a probing function
# the function should be deterministic (this simply means that function gives the same output for the same input every time),
# Probing functions must also cover all potential slots to ensure completeness.
# for every key we call the probing prob(key, 0), here 0, is the 0th attempt
# if there is a collision and a value already exists at that index, we call prob(key, 1)
# in the worst case, we have to make M calls
# since func is deterministic in nature, for the same key "k1", and attempt i the prob() will always generate the indexes to check in the same order

# example
# say prob(key1, 0) -> 5
# prob(key2, 0) -> 5, so prob(key2, 1) -> 2
# prob(key3, 0) -> 5, so prob(key3, 1) -> 2, prob(key3, 2) -> 3
# insertions and lookups are in open addressing are simple,
# if you look up k2, prob(key2, 0) -> 5, you may find key2 at 5, and that will be O(1),
# also, it is possible that you don't find key2 at 5.
# so you do prob(key2, 1) -> 2, and again, you may, or may not find k2.
# avg case, insertion and look-up both will be O(k) (here, k is the average number of collisions by the probing function)
# the selection of a good probing function is crucial for open addressing.

# IMP
# All deletes in open addressing are "SOFT DELETES"
# if you do a regular (hard) delete, say key1
# you will empty that index, so ind 5 will be empty
# now if you try to get key2
# prob(key2, 0) -> 5, but 5 is empty, so you would think that dict does not have k2
# hence we need to differentiate between an empty index and a deleted index
# hence we use a concept of soft delete.
# the simplest way to do so is put -1 for deleted index values.

# advantage is that we don't use an auxiliary storage like Linkedlist or balanced binary tree like chaining, 
# saving space and complexity of operations
# disadvantage is that max number of keys = M, while in chaining, you can have unlimited keys
# (disclaimer, you can technically still increase the size of the array, but that comes with its associated costs)
# (which just like a cache, could involve recomputing the index of all keys, as the probing function changes to account for the new arr size)

# Again, the efficiency of the open addressing is dependent upon its underlying probing function
# There are three common types of probing functions.


########################################## Probing: LINEAR PROBING ###############################################
# A general probing function is f(k, i) = j.     (k=key, i = attempt, j = index)
# Linear probing function has the form, 
# f(k, i) = (h(k) + i) % m                       (h = hashing function, m = no of slots in dic/arr)

# Linear Probing is a technique where, 
# If the array has 8 indexes (0, to 7) and a p(key=25, i=0) gives index j=3,
# and the index is already occupied, p(key=25, i=1) will give index 4, and p(key=25, i=2) will give index 5
# and the linear probing function will go from the index j to the last index m sequentially and try placing the element
# if it can't, it warps to the start, goes from index 0 to index j-1 sequentially, and tries to place the element.

# key insertion: If the calculated slot is occupied, move to the next slot sequentially until an empty slot is found.

# key lookup: 
# Calculate the initial slot using the hash function.
# Check the slot for the key; if not found, continue checking subsequent slots until the key is found or an empty slot is encountered.
# Stop if an empty slot is found, indicating the key is not in the table.

# worst case for insertion and lookup is O(m).

# key deletion:
# First look up the element.
# Then perform a soft delete by marking the slot as "deleted" instead of empty.
# This prevents premature termination of searches for keys that were hashed to nearby slots.

# Biggest Advantages
# While you may think that linear probing is super slow because it linearly traverses the arr.
# This is not the case

# This is because of something called "LOCALITY OF REFERENCE"
# When you first look up an index, the CPU does a memory fetch to get that index from memory to CPU for processing
# The OS works on a block level (1kb, 2kb, or 4kb blocks of data)
# so that index and a lot of neighboring indexes are sent back to the CPU cache by the OS
# Also, OS stores arrays with continuous memory allocation and not in a segmented manner.
# So, when a collision occurs, and we need to do a lookup to the next index, it is very likely present in the CPU cache
# and hence these linear lookups of the indexes are super fast.
# There are also claims that the "Locality of Reference" makes Linear Probing average time complexity as O(1)

# Problem of Linear Probing
# As expected, a bad hash function that increases collisions will make linear probing inefficient
# The problem will get worse if the arr size is large

# Linear probing suffers from "CLUSTERED COLLISIONS" / "CASCADING COLLISIONS"
# If there are three keys, 
# k1 hashing to index 2
# k2 hashing to index 2
# k3 hashing to index 3
# So, k1 hashes to 2, k2 goes to 3, and now k3 which was supposed to go through 3, will go through 4
# collisions can create clusters of filled slots, leading to long sequences of occupied slots.
# This increases the number of probes required for both insertions and lookups eventually reducing the hash table to a linear lookup.

# To minimize these problems, 
# The most common hash function used with Linear Probing is "MURMUR HASH" (see hashing func doc for details)


########################################## Probing: QUADRATIC PROBING ######################################
# The quadratic probing function is given as, 
# P(k, i) = (h(k) + (c1*i) + (c2 * i^2)) % m                           Where, c1 and c2 are constants and c2 can not be 0
# This way, instead of going linearly, we take quadratic leaps
# A big advantage is that we get the ability to minimize the effect of cascading/clustered collisions
# It still gets some benefits of locality of reference, but not as great as linear probing
# This is because the function grows quadratically so that some collisions will be in the cache but for large collisions,
# On the same index, the subsequent calls MAY go out of the CPU cache.

# NOTE: c1 = 1 and c2 = 3 are the most popular choices for quadratic probing constants.

########################################## CONFLICTS: DOUBLE HASHING TECHNIQUE ######################################
# Double hashing uses the same base concept as open addressing.
# The first hash function gives the base index, and on a collision, the second hash function provides the offset
# p(k, i) = (h1(k) + i*h2(k)) % m                                   Where h1 and h2 are hash functions
# The core idea is that using a second hash function completely randomizes the offset
# and hence, in principle, is more uniform and more immune to clustered/cascading collisions
# Also, if true uniformity is achieved, then number of collisions also reduces, increasing performance. 

# Considerations for the second hash function
# 1. It should never return 0
# 2. It should cycle through the entire arr index range (order is irrelevant)
# 3. It should be fast to compute (~ to a random number generator, to ensure uniformity)


########################################## MEASURING HASH TABLE PERFORMANCE ######################################
# An important metric of every hash table is the "LOAD FACTOR"
# Load Factor (alpha) = n/m, where n is the no of elements in the table, and m is the total available slots

## Time to resolve conflict
# In chaining, 
# alpha = the average number of elements per linked list
# time to resolve conflict = O(alpha + 1)  (alpha for traversing the linked list and 1 for adding the node) 

# In open addressing,
# With linear/quad probing and double hashing, the calculation of an exact time complexity is not practical
# However, researchers approximate that as number of elements in the arr/table increases, the number of probes
# (and subsequently) time to resolve conflict increases in an "exponential" manner
# Also, linear probing has the worst performance and double hashing has a relatively better performance 
# worst case would be O(m), assuming no infinite loops

## Cost of probing
# In chaining,
# cost of probing is high
# We use an arr of linked list heads, so we have to traverse the nodes of the linked list to find the key (linear traversal)
# Plus, it is not CPU cache friendly, as linked lists and trees are typically stored in a fragmented manner
# so we don't get any "locality of reference" benefits

# In open addressing
# Linear and quadratic hashing benefit from "locality of reference"
# For double hashing the cost is again high,
# as little to no "locality of reference" benefit plus CPU intensive as two hash functions need to be computed per key per attempt

########################################## BENCHMARKING HASH TABLE PERFORMANCE ######################################
# hence, there is no one good hash table strategy
# We have to choose the right strategy based on our use case
# The easiest way to do this is to use all the strategies for our case, compare the results, and choose the best one

# A standard benchmark test is,
# "LOOKUP TIME AS A FUNCTION OF INCREASING LOAD"

# 1. Create a hash table of size 1024
# 2. Insert n elements varying from 32 to 900
# 3. Lookup 1000 keys (keep a high miss ratio)

# General heuristics state that,
# 1. Performance for open addressing degrades quickly as alpha nears 1 (arr is getting full)
# 2. Chained approach degrades more gracefully (slow degradation in performance)
# 3. In open addressing, Linear Probing would almost always be slower than double-hashing
# 4. In open addressing, Probes will be shorter in double hashing
# 5. We can not generalize chained > open addressing as chained is not caching-friendly 
# 6. Cache friendliness becomes important when the arr/table size grows huge


########################################## OPTIMIZING CHAINING?  ######################################
# A major drawback of chained hashing is that we can not leverage the CPU cache with it
# We change chaining to be,
# An array, where every node is the head of a linked list,
# and every subsequent node in each linked list is an arr of fixed size (say 16 elements)
# This allows us to leverage the CPU cache while traversing linked lists

# NOTE: Even with this optimization,
# Chaining will be generally better for smaller arr sizes, and open addressing for larger arr sizes
# But this optimization helps to bridge the gap


########################################## HASH TABLE RESIZING  ######################################
# It is known that the performance of the hash table decreases as the table load factor increases
# So, we need to resize after a certain threshold
# However, resizing is very expensive, as we have to move a lot of keys to different indexes (as hash/prob functions will change to reflect the new size)
# A common threshold is, alpha = 0.5
# A common size increase strategy is to double the size of the current table/arr

# Q: Why do we always/mostly double the size?
# A: If we just increased the size of arr by 1 each time a key is added, 
# for creating a new array, copying the elements, and adding the element, 
# the time complexity for n operations will be O(n2) 

# Now, assume every time the arr is filled, we double the arr
# The time complexity for n operations will be O(n)

# INTERESTING!
# Q: Why is hash table size always a power of 2?
# A: Hash functions use the mod operation to bind the output to the size of the arr/table
# but for the CPU, a mod operation is expensive, as it needs to perform a long division to calculate the mod function
# To do better we exploit a formula of bitwise operations
# IMPORTANT: [number % m] = [number AND m-1] ..... WHERE m is a power of 2
# The bitwise AND is faster than mod and that's how we can speed up the hashing significantly by making sure hash table size m is a power of 2

# To keep exploiting this optimization
# hash table size is a power of 2, and when it needs to be increased, it is DOUBLED

# Q: When do we SHRINK the hash table/arr?
# A: by simple reverse engineering, if we follow the above good practice,
# if hash table size is n, it would have at max n/2 elements (load factor is 0.5)
# if we shrink it and reduce it by a factor of 2, it would have n/2 slots
# and hence should have at max n/4 elements
# but if we resize at n/4 - 1 elements, just 1 insertion will cause a resize again, and that will be poor design,
# so we go one more step back and reduce by a factor of 2 to n/8 elements
# hence the most common shrink condition is, alpha < 12.5% 


##################################### (CAN IGNORE) MY IMPLEMENTATION #################################
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

