class Solution(object):
    def isValid(self, s):
        stack = []  # Stack to keep track of opening brackets
        mapping = {')': '(', '}': '{', ']': '['}  # Mapping for closing to opening brackets

        for char in s:  # Iterate through each character in the string
            print(f"Current character: {char}")
            if char in mapping:  # If the character is a closing bracket
                # print(f"Current character: {char}")
                # Pop the top of the stack if it's not empty, otherwise assign a dummy value '#'
                top = stack.pop() if stack else '#'
                # print(f"Top of stack: {top}")
                

                # Check if the popped character matches the expected opening bracket
                if mapping[char] != top:
                    return False  # If it doesn't match, return False

            else:  # If it's an opening bracket
                print(f"Adding to stack: {char}")
                stack.append(char)  # Add it to the stack

        # If the stack is empty at the end, all brackets matched, otherwise it's invalid
        return not stack
s = "()[]{}"
solution = Solution()
print(solution.isValid(s))  # Output: True