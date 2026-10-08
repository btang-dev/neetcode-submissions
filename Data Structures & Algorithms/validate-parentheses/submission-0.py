class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # list
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } # hashmap (basically telling which bracket matches)

        for character in s:
            if character in closeToOpen:
                # make sure stack is not empty and is the matching parentheses
                # stack[-1] means the last value added in the stack
                if stack and stack[-1] == closeToOpen[character]:
                    stack.pop()
                # if they do not match/empty
                else:
                    return False
            # if we get an opening parentheses to start off, we can add as many openings as we want
            else:
                stack.append(character)
        # can only return true if stack is empty
        return True if not stack else False