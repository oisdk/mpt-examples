def combs(lst,n):
    if n >= len(lst):
        return [lst]
    elif n == 0:
        return [""]
    tail = lst[1:]
    head = lst[0]
    first_bit = [head + rec for rec in combs(tail,n-1)]
    second_bit = combs(tail,n)
    return first_bit + second_bit

def check_bit(n, num):
    return (num & (1 << n)) > 0

def nth_subseq(n, lst):
    return [ c for i, c in enumerate(lst) if check_bit(i, n)]

def subseq(lst):
    return [ nth_subseq(n,lst) for n in range(len(lst) ** 2)]

for s in subseq('abc'):
    print(''.join(s))
