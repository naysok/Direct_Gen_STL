import math
import time
import sys

from direct_gen_stl import gen_stl, grid, util, image_processing



####################################


time1 = time.time()

ut = util.UTIL()
gg = grid.Grid()
gs = gen_stl.GEN_STL()
im = image_processing.ImageProcessing()


amp = 10


# image_path = "IMAGES/500_AAA.jpg"
image_path = "IMAGES/500_STONE_11.jpg"



master_path = 'INPUT_DATA/dummy.txt'



f = open(master_path)
master_data = f.read()
f.close()

master_list = master_data.split('\n')


### Get Color to Memory, 2d_array
clrs = im.get_color_to_memory(image_path)

# print("color_i : {}".format(len(clrs)))
# print("color_j : {}".format(len(clrs[0])))




### Operate Input Data
p_src, v_src, mask = ut.point_vector_mask(master_list)

# print("p : {}".format(len(p_src)))
"""
250000 = 500x500
flatten list
"""



### Convert 2d Array
p_src = ut.list_to_2d_array(p_src)
v_src = ut.list_to_2d_array(v_src)
mask = ut.list_to_2d_array(mask)
# print("conver_2d_array p : {}".format(len(p_src)))
# print("conver_2d_array p[0] : {}".format(len(p_src[0])))



### Generate and Operate Grid
g = gg.gen_grid_from_input_grid(p_src, v_src, clrs, amp)
# print(g)





### Segment 4pt, input : 2d array
pt4s_mesh = gg.seg_pt4_masking(g, mask)


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
