class Solution:
    def calculate(self, s: str) -> int:
        final_eval = 0
        temp = 0
        op = 1
        stack = []
        for c in s:
            if c.isdigit():
                temp = temp * 10 + int(c)
            elif c in "+-":
                final_eval = final_eval + temp * op
                op = 1 if c=="+" else -1
                temp = 0
            elif c == '(':
                stack.append(final_eval) #cur number
                stack.append(op) # sign of the brackets whether its +(...) or -(...)
                final_eval = 0 # reinstantate default values
                op = 1 # reinstantate default values
            elif c == ')':
                final_eval = final_eval + temp*op
                pastop = stack.pop()
                pastsum = stack.pop()
                final_eval = pastsum + pastop*final_eval
                temp = 0
                op = 1
        return final_eval + op*temp