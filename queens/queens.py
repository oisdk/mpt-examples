def threat(x,y):
    return x[0] == y[0] or x[1] == y[1] or abs(x[0]-y[0]) == abs(x[1]-y[1])

def q(c,p):
    if c == 8:
        yield p
    else:
        for r in range(8):
            if not any(threat((c,r),x) for x in p):
                yield from q(c+1,p+[(c,r)])

sep = lambda s: s.join('───' for _ in range(8))
mid= '\n├'+sep('┼')+'┤\n'
past = set()
for soln in q(0,[]):
    result = set(soln)
    print('┌'+sep('┬')+'┐')
    mark = lambda x, y: ' ♕ ' if (x,y) in result else '   '
    print(mid.join('│'+'│'.join(mark(x,y) for x in range(8)) +'│' for y in range(8)))
    print('└'+sep('┴')+'┘')
    if input('"q" to quit, enter for another\n>>> ') == 'q': break
