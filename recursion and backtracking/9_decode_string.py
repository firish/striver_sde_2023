# LC 394

# The key idea is to walk through the string once with a helper 
# that returns the decoded substring up to the first closing bracket ']' (or the end) and the index it stopped at. 
# Each time we meet a digit k, we record it, skip the opening '[', recursively decode what is inside, and append that result k times. 

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Recursively decodes an encoded string such as '3[a2[c]]' -> 'accaccacc'.
        """
        def helper(i: int) -> tuple[str, int]:
            """Return (decoded_substring, position_after_substring)."""
            result = []
            while i < len(s) and s[i] != ']':
                if s[i].isdigit():                     # read full number (could be >9)
                    k = 0
                    while s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1
                    i += 1                             # skip the '['
                    decoded, i = helper(i)             # decode inside brackets
                    result.append(decoded * k)         # repeat it k times
                    i += 1                             # skip the ']'
                else:                                  # plain character
                    result.append(s[i])
                    i += 1
            return "".join(result), i                  # stop at ']' or end

        decoded, _ = helper(0)
        return decoded

