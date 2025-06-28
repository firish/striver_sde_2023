## Binary Operations and Uses

### Ones Complement

**One’s-complement** simply flips every bit (0 ↔ 1).  
In an 8-bit word, +5 is 0000 0101, so –5 becomes 1111 1010.  
Addition can proceed with the usual ripple-carry adder, and the same circuit that handles unsigned overflow can detect signed overflow by looking at the carry into and out of the sign bit.  

The drawback is that it produces two different patterns for zero (0000 0000 and 1111 1111), 
which forces extra “end-around carry” steps in arithmetic and complicates comparisons.  

Although no mainstream CPU still uses one’s complement for general arithmetic.
Its property that “all-ones” is –0 makes it perfect for checksums: 
Internet protocols such as IPv4, TCP, and UDP sum 16-bit words using one’s-complement addition so that a missing or flipped bit changes the final word from 1111 1111 to something else, flagging corruption.

### Twos Complement

**Two’s-complement** goes one step further: 
after flipping the bits you add one.  
The same +5 (0000 0101) turns into 1111 1011.  
That extra +1 eliminates the negative zero—there is now only 0000 0000—so every non-zero pattern has exactly one meaning.  

Even better, the most significant bit doubles as a sign bit *and* a weight of –2ⁿ⁻¹, 
so addition, subtraction, and multiplication can all ignore whether a value is signed or unsigned; the hardware just re-interprets the result.  

Overflow is detected with a single XOR of the carry-in and carry-out of the sign bit, and sign-extension (copying the sign bit when widening to more bits) preserves the numeric value automatically.  
Because it simplifies both logic design and compiler code generation, two’s-complement has become universal in modern CPUs, GPUs, and embedded microcontrollers.

In day-to-day programming, you rarely think about either encoding, 
but they are working invisibly whenever you store an `int` in memory, right-shift a signed value, or rely on wrap-around arithmetic in signal processing. 

Summary:
One’s-complement lives on in networking and some error-checking algorithms.
While two’s-complement underpins virtually every integer operation executed by contemporary digital hardware.

