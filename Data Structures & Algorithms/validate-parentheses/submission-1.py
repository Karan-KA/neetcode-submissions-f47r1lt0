class Solution:
    def isValid(self, s: str) -> bool:

        dictpair = { '{' : '}',
                    '[':']',
          '(':')'
        }

        stack = []

        for bracket in s:
            if bracket not in dictpair.keys():
                if stack:
                    if dictpair[stack[-1]] == bracket:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False