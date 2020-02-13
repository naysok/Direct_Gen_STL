import numpy as np
import itertools
import time


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
    stl.append(pt2stl_pt(p0))
    stl.append(pt2stl_pt(p2))
    stl.append(pt2stl_pt(p1))
    stl.append("endloop")
    stl.append("endfacet")

    ### mesh1
    stl.append(pt2stl_vec(vb))
    stl.append("outer loop")
    stl.append(pt2stl_pt(p2))
    stl.append(pt2stl_pt(p3))
    stl.append(pt2stl_pt(p1))
    stl.append("endloop")
    stl.append("endfacet")

    return stl


####################################


time1 = time.time()


p0 = (0, 0, 5)
p1 = (0, 10, 0)
p2 = (10, 0, 0)
p3 = (10, 10, 5)

m = mesh_4pt(p0, p1, p2, p3)


### export file
path_w = "../STL/test.stl"
# path_w = "test.txt"


### add header, footer
tmp_stl = []

header = "solid nameee"
footer = "endsolid nameee"

tmp_stl.append(header)
tmp_stl.append(m)
tmp_stl.append(footer)



### Flatten
export_stl = list(itertools.chain.from_iterable(tmp_stl))


### Export
with open(path_w, mode='w') as f:
    f.write('\n'.join(export_stl))

print("Export!!")



####################################


time2 = time.time()
print(f"Time : {time2 - time1} sec")
