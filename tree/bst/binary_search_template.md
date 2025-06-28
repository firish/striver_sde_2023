### Why there are several “binary‑search templates”

Binary search is always the same idea, but there are three common parameterisations. They differ in **how the interval is defined** and **what you do with the midpoint**, and each is convenient for a different kind of query.

| Template | Loop condition | Interval semantics | Updates | Typical purpose |
|----------|----------------|--------------------|---------|-----------------|
| **1. Closed interval** | `while l <= h` | current search space is `[l, h]`, both inclusive | `h = m ‑ 1` or `l = m + 1` | return an exact position or ‑1 if not found |
| **2. Half‑open (lower‑bound)** | `while l < h` | current space is `[l, h)`; `h` is one past the last candidate | `h = m` or `l = m + 1` | first value `≥ target` (“lower_bound”) |
| **3. Half‑open (upper‑bound)** | `while l < h` | `[l, h)` again | `h = m` or `l = m + 1`, but initialise `h = n + 1` | first value `> target` (“upper_bound”) |

---

#### When to pick which

1. **Exact‑match search (Template 1).**  
   Use when you only care *whether* `target` exists and, if so, *where*. The inclusive interval and condition `l <= h` make early returns trivial:

   ```python
   while l <= h:
       m = (l + h) // 2
       if nums[m] == target:
           return m
       elif nums[m] < target:
           l = m + 1
       else:
           h = m - 1
   return -1
   ```

2. **Leftmost occurrence / insertion point (Template 2).**  
   Many LeetCode problems, including “Search for a Range”, need the **first index whose value is ≥ target**. A half‑open interval `[l, h)` is perfect because you can discard the mid element from the right side by assigning `h = m`, yet keep it on the left by assigning `l = m + 1`. After the loop, `l` is the insertion point:

   ```python
   l, h = 0, len(nums)
   while l < h:
       m = (l + h) // 2
       if nums[m] < target:
           l = m + 1
       else:
           h = m
   # l == h is now the lower_bound
   ```

3. **Rightmost occurrence (Template 3).**  
   Symmetric to Template 2, but you search for the **first element > target**; the last `≤ target` is at `l‑1`. Initialise `h = len(nums)` or even `len(nums) + 1` to leave a sentinel slot at the right end.

   ```python
   l, h = 0, len(nums)
   while l < h:
       m = (l + h) // 2
       if nums[m] <= target:
           l = m + 1
       else:
           h = m
   rightmost = l - 1            # may be -1 if target absent
   ```

---

### Putting it together for `searchRange`

LeetCode 34, **`searchRange`**, asks for both the leftmost and rightmost indices of `target`. The idiomatic solution is two Template 2 searches—one for `target` and one for `target + 1`—or a Template 2 + Template 3 pair. Sketch:

```python
def searchRange(nums, target):
    def lower_bound(x):
        l, h = 0, len(nums)
        while l < h:
            m = (l + h) // 2
            if nums[m] < x:
                l = m + 1
            else:
                h = m
        return l

    left  = lower_bound(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]        # target absent
    right = lower_bound(target + 1) - 1
    return [left, right]
```

---

### Minor—but important—variations

* **Overflow‑safe midpoint**: `m = l + (h - l) // 2` is safer than `(l + h) // 2` in fixed‑width languages; in Python it makes no difference.
* **Biasing `mid`**: some authors use `m = (l + h + 1) // 2` when they want the midpoint to round up, which avoids infinite loops in certain “upper‑bound” searches.
* **Early exit vs. post‑processing**: Templates 2 and 3 never test `nums[m] == target` inside the loop; they finish the loop and then inspect `l` or `l‑1`. This keeps the invariant (“everything left of `l` is < target”) spotless.
* **Predicate form**: For monotone boolean functions (e.g., “is it feasible to ship in ≤ D days?”) you often write the loop on a predicate `P(mid)` instead of a value comparison, but the interval‑update logic is identical: push the boundary past the last `False` (`l = m + 1`) or before the first `True` (`h = m`).

---

#### Take‑away

Choose the template whose invariant matches the *question* you are asking:

* Need the exact index? **Template 1.**
* Need the first value ≥ x? **Template 2.**
* Need the last value ≤ x? **Template 3.**

Once you decide, stick to the corresponding loop condition and boundary updates; that way your binary searches will be correct, loop‑safe, and easy to reason about every time.
