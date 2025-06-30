## Get count of all set bits (population count / Hamming weight)


### 1. Python ≥ 3.8 one-liner   `O(1)` time¹

```python
def popcount_builtin(x: int) -> int:
    return x.bit_count()          # hardware-assisted on most CPUs
```

### 2. Kernighan’s loop O(set bits) time
```python
def popcount_kernighan(x: int) -> int:
    count = 0
    while x:
        x &= x - 1     # clears the least-significant set bit
        count += 1
    return count
```
Why it works Every x &= x-1 drops one 1-bit, so the loop runs exactly
#ones times—excellent for sparse bitsets.


## Get position of all set bits

There are two clean patterns: scan every bit or iterate only over the set bits.

### 1. Simple scan O(word size) time

```python
def positions_scan(x: int) -> list[int]:
    pos = []
    idx = 0
    while x:
        if x & 1:
            pos.append(idx)
        x >>= 1
        idx += 1
    return pos
```
Talking point Dead-simple; cost proportional to total bits (e.g. 64).

### 2. Kernighan iteration O(# ones) time

```text
x = 56
x  = 0011 1000
-x = 1100 1000 (2's complement)
and  ----------
     0000 1000
```
We can see that only the LSB is set. everything else is 0.
**`x & -x` leaves LSB and unsets everything else**

```python
def positions_kernighan(x: int) -> list[int]:
    """
    Collect indexes of all 1-bits using the 'x & -x' trick.
    """
    pos = []
    while x:
        lsb = x & -x                           # isolates least-significant 1-bit
        pos.append(lsb.bit_length() - 1)       # add the position
        x &= x - 1                             # clear the lsb bit
    return pos
```
Why it works x & -x keeps only the lowest 1-bit.
bit_length() – 1 converts that one-hot value to its index.

