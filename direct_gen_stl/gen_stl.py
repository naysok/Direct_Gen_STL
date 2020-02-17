import itertools

from . import util



class GEN_STL():


    def pt2stl_vec(self, vector):
        return "facet normal " + str(vector[0]) + " " + str(vector[1]) + " " + str(vector[2])


    def pt2stl_pt(self, point):
        return "vertex " + str(point[0]) + " " + str(point[1]) + " " + str(point[2])


    def stl_4pt(self, p0, p1, p2, p3):

        ut = util.UTIL()

        # define mesh
        stl = []

        ### calc normal vector
        va = ut.face_normal(p0, p2, p1)
        vb = ut.face_normal(p0, p2, p1)

        ### mesh0
        stl.append(self.pt2stl_vec(va))
        stl.append("outer loop")
        stl.append(self.pt2stl_pt(p1))
        stl.append(self.pt2stl_pt(p2))
        stl.append(self.pt2stl_pt(p0))
        stl.append("endloop")
        stl.append("endfacet")

        ### mesh1
        stl.append(self.pt2stl_vec(vb))
        stl.append("outer loop")
        stl.append(self.pt2stl_pt(p1))
        stl.append(self.pt2stl_pt(p3))
        stl.append(self.pt2stl_pt(p2))
        stl.append("endloop")
        stl.append("endfacet")

        return stl

    


    def gen_stl(self, pt4s_mesh):

        meshes = []

        for num in range(len(pt4s_mesh)):
            m = self.stl_4pt(pt4s_mesh[num][0], pt4s_mesh[num][1], pt4s_mesh[num][2], pt4s_mesh[num][3])
            meshes.append(m)

        ### Flatten
        meshes = list(itertools.chain.from_iterable(meshes))
        # print(meshes)

        return meshes


    def format_stl(self, meshes):

        export_stl = []

        header = "solid nameee"
        footer = "endsolid nameee"

        export_stl.append(header)

        for flatten in range(len(meshes)):
            export_stl.append(meshes[flatten])

        export_stl.append(footer)

        return export_stl




