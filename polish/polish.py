from operator import add, mul, sub, floordiv
import operator

ops = {'+': add,
       '*': mul,
       '-': sub,
       '/': floordiv}

stack = []
for op in input().split():
    try:
        stack.append(int(op))
    except ValueError:
        stack.append(ops[op](stack.pop(), stack.pop()))
print(stack[0])

