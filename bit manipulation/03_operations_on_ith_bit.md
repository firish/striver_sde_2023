## Operations on the ith bit

### Check if the ith bit is set

There are multiple ways to check this. But prolly, the easiest way is to and the ith bit with one.
If result is 0, bit is unset, if result is non-zero, ith bit is set.

Number = x = 13, representation = 8-bit, check for target = k = 3rd bit.

`x = 0000 1101`

Step 1:
- So the first step involves creating a mask.
- This is done by left shift (or right shift)
- left shift is basically shifting all bits to left by 1, this is equivalent to multiplication by 2.
- here k = 3
- for the mask simply do `1 << k`
- `1 = 0000 0001`
- `1 << k = 0000 1000`

Step 2:
- Mask has been created, so simply `And` the bits
```text
13 & (1 << k)

0000 1101
0000 1000
---------
0000 1000
```
- the result is non-zero, so the bit was set.

code:
```python
def is_bit_set(num, k):
    return num & (1 << k) != 0
```


