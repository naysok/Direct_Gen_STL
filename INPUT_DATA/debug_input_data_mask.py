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
mask = ut.list_to_2d_array(mask)


w = len(mask)
h = len(mask[0])

im = Image.new('RGB', (w, h), (0, 0, 0))
draw = ImageDraw.Draw(im)


for i in range(w):
    for j in range(h):

        # print(mask[i][j])

        if mask[i][j] == "1":
            # print("True!!")
            draw.point((i, j), fill = (255, 255, 255))
        
        else:
            draw.point((i, j), fill = (0, 0, 0))


im.show()