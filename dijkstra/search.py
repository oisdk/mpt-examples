# from algorithm at http://www.redblobgames.com/pathfinding/a-star/introduction.html

from queue import PriorityQueue

def heuristic(px, py):
    return abs(px[0]-py[0]) + abs(px[1]-py[1])

class Graph:
    def __init__(self, size, boundaries):
        self._size = size
        self._grid = [ [ True for _ in range(size) ] for _ in range(size) ]
        for y, x in boundaries:
            self._grid[y][x] = False

    def neighbors(self,point):
        py, px = point
        for y in (py-1,py,py+1):
            for x in (px-1,px,px+1):
                if (y,x) != point and \
                   0 <= y < self._size and \
                   0 <= x < self._size and \
                   self._grid[y][x]:
                    yield (y,x)

    def cost(self,px,py):
        return abs(complex(*px)-complex(*py))

    def _draw(self,pts=None):
        yield '┌'
        for x in range(self._size-1):
            yield '──┬'
        yield '──┐'
        for y in range(self._size):
            yield '\n│'
            for x in range(self._size):
                if pts and (y,x) in pts:
                    yield '..'
                elif self._grid[y][x]:
                    yield '  '
                else:
                    yield '**'
                yield '│'
            if y == self._size-1:
                yield '\n└──'
                yield '┴──' * (self._size-1)
                yield '┘'
            else:
                yield '\n├──'
                yield '┼──' * (self._size-1)
                yield '┤'


    def __str__(self):
        return ''.join(self._draw())

def path(came_froms,point):
    while True:
        yield point
        try:
            point = came_froms[point]
        except KeyError:
            break


def search(start, goal, graph):
    frontier = PriorityQueue()
    frontier.put((0,start))
    came_from = {}
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()


        if current == goal:
            print(''.join(graph._draw(set(path(came_from,current)))))
            return list(reversed(list(path(came_from,current))))

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((priority,next))
                came_from[next] = current

    return None

g = Graph(9, [(3,3),(2,3),(4,3),(5,3),(6,3),(2,3),(1,3),(0,3)])
print(search((0,0),(5,5),g))
