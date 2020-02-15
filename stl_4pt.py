import time

from direct_gen_stl import gen_stl, grid


####################################


time1 = time.time()


gg = grid.Grid()
gs = gen_stl.GEN_STL()


resolution = 100


### Generate Grid
g = gg.gen_grid(resolution)

"""
100 x 100 >> 0.3 Sec
500 x 500 >> 8 Sec
1000 x 1000 >> 40 Sec
"""


### Segment 4pt
pt4s_mesh = gg.seg_pt4(g)


### Gen STL
meshes = gs.gen_stl(pt4s_mesh)


### Format, Add header, footer
export = gs.format_stl(meshes)


### export file
path_w = "STL/plane.stl"
# path_w = "test.stl"

### Export
with open(path_w, mode='w') as f:
    f.write('\n'.join(export))

print("Export!!")


####################################


time2 = time.time()
print(f"Time : {time2 - time1} sec")
