import time


from direct_gen_stl import gen_stl, grid, util, image_processing


####################################


time1 = time.time()


gg = grid.Grid()
gs = gen_stl.GEN_STL()
im = image_processing.ImageProcessing()


resolution = 500


# image_path = "IMAGES/500_AAA.jpg"
image_path = "IMAGES/500_STONE_11.jpg"


### Get Color to Memory
clrs = im.get_color_to_memory(image_path)

### Generate Grid
### gen_grid_image(resolution, color, amp)
g = gg.gen_grid_image(500, clrs, 30)


"""
100 x 100 >> 0.3 Sec
500 x 500 >> 8 Sec
1000 x 1000 >> 40 Sec
"""


time2 = time.time()


### Segment 4pt
pt4s_mesh = gg.seg_pt4(g)


### Gen STL
meshes = gs.gen_stl(pt4s_mesh)


### Format, Add header, footer
export = gs.format_stl(meshes)


### export file
# path_w = "STL/images.stl"
path_w = "test.stl"


### Export
with open(path_w, mode='w') as f:
    f.write('\n'.join(export))


print("Export!!")



####################################


time3 = time.time()
print(f"Time (Image Prcessing) : {time2 - time1} sec")
print(f"Time (Generate STL) : {time3 - time2} sec")

