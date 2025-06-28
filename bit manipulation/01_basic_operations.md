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


## Logic Gates and Binary

Think of the four basic bit-wise operators—AND, OR, XOR, and NOT—as the tiny “switchboards” inside every digital device. 
Each one compares (or flips) individual bits, letting hardware do jobs that would be clumsy or slow if you treated the numbers only as whole values. 

Here’s how each operation earns its keep in the real world.

### AND
What it does: Compares two bits; the result is 1 only when both bits are 1.
Why you’d use it: To keep (mask) the bits you care about and zero-out everything else.

Everyday examples:
- Permission flags – Operating systems store read/write/execute rights as individual bits. To see whether a file is writable you AND its flag byte with 0000 0010; the result is non-zero only if that specific bit is set.
- Color extraction – A 24-bit RGB color like 0x7F3BCD packs red, green, and blue into one integer. color AND 0x00FF00 isolates just the green channel.
- Why not just divide or mod? Because a single AND on the raw bits is faster and uses almost no hardware.


### OR
What it does: Produces 1 if either input bit is 1.
Why you’d use it: To turn specific bits on without disturbing the rest.

Everyday examples
- Setting options – Suppose a microcontroller’s control register turns an LED on with bit 0 and starts a motor with bit 3. Writing reg = reg OR 0b0000 1001 flips on both features while leaving all other settings untouched.
- Building composite values – Network protocols build header fields by OR-ing together smaller constants; you can set the “don’t fragment” and “more fragments” flags in an IPv4 packet with one OR.


### XOR (exclusive-or)
What it does: Outputs 1 when the two bits are different.
Why you’d use it: To toggle bits, detect differences, or blend data in a way that’s easy to reverse.

**NOTE**
number ^ 0 = number
number ^ 1 = toggled number

Everyday examples
- Checksums & parity – Hard drives XOR every byte in a sector to store one extra “parity byte.” If a single bit flips, another XOR of all bytes reveals the error.
- Cryptography & image blending – The one-time pad cipher (in its purest form) encrypts text by XOR-ing it with a secret key; XOR the result with the same key and the plaintext pops right back out. 
Bit toggling – value XOR 0xFF flips every bit; value XOR 0x04 flips just bit 2. Handy for inverting pixels or switching a GPIO pin’s state.



### NOT
What it does: Flips each bit by itself: 0 → 1, 1 → 0.
Why you’d use it: To create the logical opposite of a value or to build masks on the fly.

**NOTE**
```math
~x   ==   –x – 1
```
| decimal | 8-bit picture | after NOT   | decimal meaning of result\* |
| ------- | ------------- | ----------- | --------------------------- |
| 6       | `0000 0110`   | `1111 1001` | –7                          |
| 9       | `0000 1001`   | `1111 0110` | –10                         |

**NOTE**
Another interesting thing:
Subtraction via addition
Inside the ALU, a – b is done as a + (~b + 1). The NOT gate gives you ~b “for free,” then one adder does the rest.

Everyday examples
- Forming complements – Two’s-complement negation is really “NOT the bits, then add 1.” Every ALU has a NOT gate for that first step.
- Quick subtraction tricks – In low-level code, clearing all but a few bits can be easier as value AND (NOT mask) instead of computing the mask manually.
- Signal inversion – In electronics, an inverting buffer is just the hardware version of NOT, turning a high voltage into low and vice-versa.


### Why hardware loves these operators
- Simplicity – Each operation is just a handful of transistors, so they run in a single clock tick.
- Parallelism – A 64-bit AND processes all 64 bits at once; speed is the same as for 8 bits.
- Building blocks – With AND, OR, XOR, and NOT you can synthesize any logical function. Algebraically, they are the LEGO bricks of computing.



