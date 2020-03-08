import math
import time
from PIL import Image, ImageDraw

import sys
sys.path.append("../")

from direct_gen_stl import gen_stl, grid, util, image_processing

ut = util.UTIL()
gg = grid.Grid()
gs = gen_stl.GEN_STL()
im = image_processing.ImageProcessing()





time1 = time.time()



master_path = "dummy.txt"

f = open(master_path)
master_data = f.read()
f.close()

master_list = master_data.split('\n')


### Operate Input Data
p_src, v_src, mask = ut.point_vector_mask(master_list)

"""
250000 = 500x500
flatten list
"""

### Convert 2d Array
p_src = ut.list_to_2d_array(p_src)



### Segment 4pt
pt4s_mesh = gg.seg_pt4(p_src)


### Gen STL
meshes = gs.gen_stl(pt4s_mesh)


### Format, Add header, footer
export = gs.format_stl(meshes)


### export file
path_w = "debug.stl"
# path_w = "test.stl"

### Export
with open(path_w, mode='w') as f:
    f.write('\n'.join(export))

print("Export!!")


####################################


time2 = time.time()
print(f"Time : {time2 - time1} sec")