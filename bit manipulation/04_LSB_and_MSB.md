## Cleat the LSB / set right-most bit

This is very simple. 
x = 56
x = 0011 1000

Now, not this relationship between x and x-1:
x-1 = 55
x-1 = 0011 0111

**For a and x-1, the LSB is 0, every bit to left is same, and every bit to right is 1.**

Hence, if we & them, the LSB will be cleared.
x & x-1

```text
0011 1000
0011 0111
---------
0011 0000
```

```python
def _clear_lsb(x):
    return x and (x-1)
```


## Clear the MSB / set left-most bit

x = 56
x = 0011 1000

Steps:
- find the MSB index.
    - **In python, there is a built in function to do this, `x.bit_length() - 1`**
- creat a mask
    - set the bit at the target index to 1. `(1 << (x.bit_length() - 1))`
    - not the values so everything is 1 except the index: `~(1 << (x.bit_length() - 1))`
- simply, and x and the mask

```text
x = 0011 1000

k = x.bit_length() - 1 (here, k = 5)

mask = ~(1 << (x.bit_length() - 1)) (1101 1111)

0011 1000
1101 1111
---------
0001 1000
```

```python
def _clear_msb(x):
    k = x.bit_length() - 1
    return x and (not (1 << k))
```
