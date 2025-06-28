# Swapping two numbers classic

```python
temp = a
a = b
b = temp

# one line syntax
a, b = b, a
```

~~~python
# XOR swap: exchanges the values of a and b in-place
a = a ^ b
b = a ^ b
a = a ^ b
~~~

### Why it works  
XOR (`^`) has two algebraic properties that make the trick possible:  

1. **Self-canceling** – `x ^ x = 0`  
2. **Identity element** – `x ^ 0 = x`  


step 1, 
`a = a ^ b`


step 2, 
`b = a ^ b`
but here, `a = a ^ b`, so,
`b = a ^ b ^ b`
But `b ^ b` is 0
so, `b = a` (one number swapped)

step 3,
`a = a ^ b`
Here, `a` is still `a ^ b`
Here, `b` is now `a` (step 2)
so, the eq becomes,
`a = a ^ b ^ a`
Now, `a ^ a = 0`
Hence, 
`a = b` (both numbers swapped)

The benefit is no extra money is spent to swap numbers this way.
