import heapq

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def do_move(mh, a, b):
    mh += [v]
    return (distance() + len(mh), cpos, mh)

def perform_move(visited, H, G, mh, p, t, a, b):
    if G[  p[0] + a  ][  p[1] + b  ] == 0:
        npos = [  p[0] + a, p[1] + b  ]
        R = [ distance(npos, t) + len(mh), npos, mh+[npos] ]
        if str(R[1]) not in visited:
            heapq.heappush(H, R)

def all_moves(G, visited, H, p, path, target):
    gr, gc = len(G), len(G[0])

    if p[0] < gc-1:
        perform_move(visited, H, G, path, p, target,  1,  0)
    if 0 < p[0]:
        perform_move(visited, H, G, path, p, target, -1,  0)
    if p[1] < gr-1:
        perform_move(visited, H, G, path, p, target,  0,  1)
    if 0 < p[1]:
        perform_move(visited, H, G, path, p, target,  0, -1)

def heapsolve(grid, spos, epos):
    H = [(distance(spos, epos), spos, [spos[:]])]
    heapq.heapify(H)
    D, V = 100, []
    visited = set()
    visited.add(str(spos))
    while D > 0 and len(H) > 0:
        V = heapq.heappop(H)
        D = distance( V[1], epos )
        visited.add(str(V[1]))
        all_moves(grid, visited, H, V[1], V[2][:], epos)
    return V[2] if D == 0 else [spos]

def simple_test():
    grid = [ [0]*8
        ,[1]*7 + [0]
        ,[0]*8
        ,[0]+ [1]*7
        ,[0]*8
        ,[1]*7 + [0]
        ,[0]*8
        ,[0]+ [1]*7
        ]

    for row in grid:
        print([i if i == 0 else 1 for i in row])

    # for i in range(1000): #try timing
    path = heapsolve(grid, [2,2], [6,0])
    print(path)

if __name__ == '__main__':
    simple_test()