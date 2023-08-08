class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :param tokens: an array of strings tokens represents an arithmetic 
                        expression in a Reverse Polish Notation:
                        https://en.wikipedia.org/wiki/Reverse_Polish_notation
        :return: an integer that represents the value of the expression.
        """

        stack = []
        for token in tokens:
            # if token is operation, pop 2 nums from stack and calculate the result,
            # then push it to stack.
            if token in ["+", "-", "*", "/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "/":
                    stack.append(int(num1 / num2))
                if token == "*":
                    stack.append(num1 * num2)
                if token == "-":
                    stack.append(num1 - num2)
            else:
                stack.append(int(token))
        return stack[0]
