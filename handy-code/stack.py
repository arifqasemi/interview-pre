class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['*','-','+','/']
        for n in tokens:
            if n not in "+-*/":
                stack.append(int(n))

            else:
                a = stack.pop()
                b = stack.pop()
                if n == '+':
                    result = b + a
                elif n == '-':
                    result = b - a
                elif n == '*':
                    result = b * a
                elif n == '/':
                    result = int(float(b) / a)
                stack.append(result)

        return stack[0]
        