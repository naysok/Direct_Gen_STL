def gen_grid(count):
    grid = []

    for i in range(count):

        sub = []        
        for j in range(count):
            p = (i, j, 0)
            sub.append(p)
        
        grid.append(sub)

    return grid


def seg_pt4(grid):

    pt4s = []

    for u in range(len(grid) - 1):
        for v in range(len(grid[0]) - 1):
            pt4 = []

            pt4.append(g[u][v])
            pt4.append(g[u+1][v])
            pt4.append(g[u][v+1])
            pt4.append(g[u+1][v+1])

            pt4s.append(pt4)

    return pt4s


g = gen_grid(10)
pt4s = seg_pt4(g)

print(pt4s)
print(pt4s[0])
print(len(pt4s))


