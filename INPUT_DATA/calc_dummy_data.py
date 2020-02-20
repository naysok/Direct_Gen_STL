import math
import time

import sys
sys.path.append("../")

from direct_gen_stl import gen_stl, grid, util, image_processing




def create_dummy_data_by_cylinder(grid, mask):

    data = []
    ax = []
    ay = []
    az = []
    m = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            point = grid[i][j]
            x = '{:.8f}'.format(point[0])
            y = '{:.8f}'.format(point[1])
            z = '{:.8f}'.format(point[2])
            ax = x
            ay = y
            az = z
            m = mask[i][j]

            pt_vec_mask = (str(x) + "," + str(y) + "," + str(z) + ","
                + str(ax) + "," + str(ay) + "," + str(az) + "," + str(m))

            # print(pt_vec_mask)
            data.append(pt_vec_mask)

    return data




####################################


time1 = time.time()

gg = grid.Grid()
gs = gen_stl.GEN_STL()
im = image_processing.ImageProcessing()


resolution = 500
raddd = 100

image_path = []
mask_path = "../IMAGES/500_AAA.jpg"


g = gg.gen_grid_cylinder(resolution, raddd)
m = im.get_mask(mask_path, 1)

dummy = create_dummy_data_by_cylinder(g, m)
# print(dummy)


### Export
path_d = "dummy.txt"
with open(path_d, mode='w') as f:
    f.write('\n'.join(dummy))
print("Export!!")




sys.exit()

### Segment 4pt
pt4s_mesh = gg.seg_pt4(g)


### Gen STL
meshes = gs.gen_stl(pt4s_mesh)


### Format, Add header, footer
export = gs.format_stl(meshes)


### export file
# path_w = "STL/plane.stl"
path_w = "test.stl"

### Export
with open(path_w, mode='w') as f:
    f.write('\n'.join(export))

print("Export!!")


####################################


time2 = time.time()
print(f"Time : {time2 - time1} sec")
