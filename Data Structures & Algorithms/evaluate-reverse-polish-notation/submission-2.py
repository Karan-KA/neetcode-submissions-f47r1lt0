class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens:
            if element not in "+-/*":
                stack.append(int(element))

            else:
                b = stack.pop()
                a = stack.pop()

                if element == '+' : stack.append(a+b)
                if element == '-' : stack.append(a-b)
                if element == '*' : stack.append(a*b)
                if element == '/' : stack.append(int(a/b))

        return (stack[0])


