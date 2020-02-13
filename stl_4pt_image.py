import math
import numpy as np
import itertools
import time
from PIL import Image, ImageDraw


def remap_number(src, old_min, old_max, new_min, new_max):
    return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


def pt_pt_subtract(pt0, pt1):
    pt = (pt1[0] - pt0[0], pt1[1] - pt0[1], pt1[2] - pt0[2])
    return pt


def pt2stl_vec(vector):
    return "facet normal " + str(vector[0]) + " " + str(vector[1]) + " " + str(vector[2])

def pt2stl_pt(point):
    return "vertex " + str(point[0]) + " " + str(point[1]) + " " + str(point[2])


def face_normal(p0, p1, p2):
    v1 = pt_pt_subtract(p1, p0)
    v2 = pt_pt_subtract(p2, p0)

    # ベクトル同士の外積
    n0 = v1[1] * v2[2] - v1[2] * v2[1]
    n1 = v1[2] * v2[0] - v1[0] * v2[2]
    n2 = v1[0] * v2[1] - v1[1] * v2[0]

    n = (n0, n1, n2)

    return n


def mesh_4pt(p0, p1, p2, p3):
    # define mesh
    stl = []

    ### calc normal vector
    va = face_normal(p0, p2, p1)
    vb = face_normal(p0, p2, p1)

    ### mesh0
    stl.append(pt2stl_vec(va))
    stl.append("outer loop")
    stl.append(pt2stl_pt(p1))
    stl.append(pt2stl_pt(p2))
    stl.append(pt2stl_pt(p0))
    stl.append("endloop")
    stl.append("endfacet")

    ### mesh1
    stl.append(pt2stl_vec(vb))
    stl.append("outer loop")
    stl.append(pt2stl_pt(p1))
    stl.append(pt2stl_pt(p3))
    stl.append(pt2stl_pt(p2))
    stl.append("endloop")
    stl.append("endfacet")

    return stl


def get_color_to_memory(img):

    size = img.size

    cl_l = []

    for i in range(size[1]):

        cl = []

        for j in range(size[0]):
            c = img.getpixel((j, i))
            cl.append(c)
        
        cl_l.append(cl)
    
    return cl_l


def gen_grid(count):

    grid = []

    for i in range(count):
        sub = []
        for j in range(count):
            p = (i, j, 0)
            sub.append(p)
        grid.append(sub)
    
    return grid



def gen_grid_sin(count):

    grid = []

    for i in range(count):
        sub = []
        for j in range(count):
            si = math.sin(i)
            sj = math.sin(j)
            p = (i, j, si+ sj)
            sub.append(p)
        grid.append(sub)
    
    return grid

###
def gen_grid_image(count, colors, amp):

    grid = []

    for i in range(count):
        sub = []
        for j in range(count):

            ### COLOR CHANNEL
            # RR, GG, BB, AA = colors[i][j]
            RR, GG, BB = colors[i][j]

            RR = remap_number(RR, 0, 255, 0, amp)
            p = (i, j, RR)
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


def gen_stl(pt4s_mesh):
    meshes = []

    for num in range(len(pt4s_mesh)):
        m = mesh_4pt(pt4s_mesh[num][0], pt4s_mesh[num][1], pt4s_mesh[num][2], pt4s_mesh[num][3])
        meshes.append(m)

    ### Flatten
    meshes = list(itertools.chain.from_iterable(meshes))
    # print(meshes)

    return meshes



####################################


time1 = time.time()

# image_path = "IMAGES/500_AAA.jpg"
image_path = "IMAGES/500_STONE_11.jpg"
# image_path = "IMAGES/1000_ROCK.jpg"


img = Image.open(image_path)

### Get Color to Memory
clrs = get_color_to_memory(img)

### Generate Grid
# gen_grid_image(resolution, color, amp)
g = gen_grid_image(500, clrs, 30)
# print(g)

"""
100 x 100 >> 0.3 Sec
500 x 500 >> 8 Sec
1000 x 1000 >> 40 Sec
"""


time2 = time.time()




### Segment 4pt
pt4s_mesh = seg_pt4(g)


### Gen STL
meshes = gen_stl(pt4s_mesh)


### Add header, footer
export_stl = []

header = "solid nameee"
footer = "endsolid nameee"

export_stl.append(header)
for flatten in range(len(meshes)):
    export_stl.append(meshes[flatten])
export_stl.append(footer)



### export file
path_w = "STL/images.stl"
# path_w = "test.txt"


### Export
with open(path_w, mode='w') as f:
    f.write('\n'.join(export_stl))


print("Export!!")



####################################


time3 = time.time()
print(f"Time (Image Prcessing) : {time2 - time1} sec")
print(f"Time (Generate STL) : {time3 - time2} sec")

