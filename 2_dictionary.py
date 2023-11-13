# The hash function

# A very important part of the dict is its hash function f1()
# For Python, this is written in C and is very complex

# A simplified version is as follows,

def simple_hash(key):

    if isinstance(key, int):
        return key & 0xffffffff
    
    elif isinstance(key, float):
        # Convert the float to its binary representation (as an integer)
        float_as_int = int.from_bytes(key.hex().encode(), 'little')
        return simple_hash(float_as_int)
    
    elif isinstance(key, str):
        hash_value = 0
        for char in key:
            hash_value = hash_value * 31 + ord(char)
        return hash_value & 0xffffffff
    
    elif isinstance(key, tuple):
        hash_value = 0x345678
        for item in key:
            hash_value = (1000003 * hash_value) ^ simple_hash(item)
        hash_value ^= len(key)
        return hash_value & 0xffffffff
    
    else:
        raise TypeError(f'Unhashable type: {type(key)}')

