## Check whether a number is a **power of 2**

A power-of-two has exactly **one** set bit
```text
1 = 0000 0001
2 = 0000 0010
4 = 0000 0100
```

Note: **Hence, if you clear the LSB, the result for a perfect square will always be 0.**

### 1. Bit-trick one-liner `O(1)` time
```python
def is_power_of_two(x: int) -> bool:
    return x > 0 and (x & (x - 1)) == 0
```

## Odd and even
```text
x = 5 =  0000 0101
x = 7 =  0000 0111
x = 31 = 0001 1111
x = 69 = 0100 0101
```
Notice: For odd numbers, last bit is always 1.

```python
def is_odd(x: int)  -> bool: return (x & 1) == 1   # O(1)
def is_even(x: int) -> bool: return (x & 1) == 0   # O(1)
```


