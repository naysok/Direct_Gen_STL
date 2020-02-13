def gen_grid(count):
    grid = []

    for i in range(count):

        sub = []        
        for j in range(count):
            p = (i, j, 0)
            sub.append(p)
        
        grid.append(sub)

    return grid


g = gen_grid(10)

print(g)