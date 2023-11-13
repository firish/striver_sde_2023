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
