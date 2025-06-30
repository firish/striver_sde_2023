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

0011 1000
0011 0111
---------
0011 0000

```python
def _clear_lsb(x):
    return x and (x-1)
```


## Clear the MSB / set left-most bit

