def group(lst):
    acc = []
    for c in lst:
        if acc != [] and c == acc[-1][0]:
            acc[-1] += c
        else:
            acc.append(c)
    return acc

def look_say(seed):
    while True:
        old = str(seed)
        new = int(''.join(str(len(g)) + g[0] for g in group(old)))
        yield new
        seed = new

i = 0
lim = 100
for x in look_say(123):
    print(x)
    if i > 10:
        break
    i += 1
