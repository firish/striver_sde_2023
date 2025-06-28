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
    return num and (1 << k) != 0
```


### Set the ith bit

number = 14
n = `0000 1110`, and `k=5`

step 1:
- So the first step involves creating a mask.
- This is done by left shift (or right shift)
- here k = 3
- mask = `(1 << k)`

Step 2:
- Mask has been created, so simply `OR` the bits
```text
13 OR (1 << k)

0000 1110
0010 0000
---------
0010 1110
```
- ith bit was set

code:
```python
def _set_bit(num, k):
    return num or (1 << k)
```


### Clear the ith bit

number = 17
n = `0001 0001`, and `k=4`

step 1:
- So the first step involves creating a mask.
- This is done by left shift (or right shift)
- here k = 5
- mask = `~(1 << k)`
- here we take the not, so that every bit is set except kth bit

Step 2:
- Mask has been created, so simply `AND` the bits
```text
17 AND ~(1 << k)

0001 0001
1110 1111
---------
0000 0001
```
- ith bit was cleared

code:
```python
def _clear_bit(num, k):
    return num and (not (1 << k))
```


### Toggle the ith bit

number = 22
n = `0001 0110`, and `k=6`

step 1:
- So the first step involves creating a mask.
- This is done by left shift (or right shift)
- here k = 6
- mask = `(1 << k)`

Step 2:
- Mask has been created, so simply `XOR` the bits
```text
22 XOR (1 << k)

0001 0110
0100 0000
---------
0101 0110
```
- ith bit was cleared

code:
```python
def _toggle_bit(num, k):
    return num xor (1 << k)
```

**Cheatsheet**
```text
Clear bit k   :  num & ~(1 << k)
Set   bit k   :  num |  (1 << k)
Toggle bit k  :  num ^  (1 << k)
Test   bit k  : (num &  (1 << k)) != 0
```
