# LC Medium
# lC 394: https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        ind, limit = 0, len(s)
        while ind < limit:
            char = s[ind]
            # Get the enclosed strings
            if char != ']':
                stack.append(char)
            else:
                enclosed_str = ""
                multiplier = ""
                while stack[-1] != '[':
                    enclosed_str = stack.pop() + enclosed_str
                stack.pop() #  pop the [
                while len(stack) > 0 and stack[-1].isnumeric():
                    multiplier = stack.pop() + multiplier
                if len(enclosed_str) > 0 and len(multiplier) > 0:
                    enclosed_str = enclosed_str*int(multiplier)
                stack.append(enclosed_str)
            ind += 1
            
        return ''.join(stack)



