def fact_slow(n):

    if n == 0:
        return 1
    else:
        return n * fact_slow(n - 1)


fact_dict = {0:1}


def fact_memo(n):
    global fact_dict
    if n in fact_dict:
        return fact_dict[n]
    else:
        result = n * fact_memo(n-1)
        fact_dict[n] = result
        return result


def fact_iter(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


fact_list = [1]


def fact_iter_memoized(n):

    while n >= len(fact_list):
        fact_list.append(len(fact_list)*fact_list[-1])
    return fact_list[n]


from itertools import accumulate, count
from functools import reduce
from operator import __mul__


def fact_iter_idiom(n):
    return reduce(__mul__, range(1, n + 1), 1)

fact_iter = accumulate(count(1), __mul__)

def fact_memo_idiom(n):
    while n >= len(fact_list):
        fact_list.append(next(fact_iter))
    return fact_list[n]

print(fact_memo(500))
print(fact_memo(987))
