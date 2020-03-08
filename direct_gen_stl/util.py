#########################################################
### Utilities                                         ###
###                                                   ###
###                                                   ###
#########################################################


import math


class UTIL():


    def remap_number(self, src, old_min, old_max, new_min, new_max):
        return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


    def split_list(self, l, n):

        # https://www.python.ambitious-engineer.com/archives/1843 
        for idx in range(0, len(l), n):
            yield l[idx:idx + n]

        return l


    def list_to_2d_array(self, l):

        num = int(math.sqrt(len(l)))
        # print("sqrt : {}".format(num))

        array_2d = list(self.split_list(l, num))
        # print("i_count : {}".format(len(array_2d)))
        # print("j_count : {}".format(len(array_2d[0])))

        return array_2d


    def pt_pt_subtract(self, pt0, pt1):
        pt = [
            float(pt1[0]) - float(pt0[0]),
            float(pt1[1]) - float(pt0[1]),
            float(pt1[2]) - float(pt0[2])]
        return pt


    def vector_multiplicate(self, vector, value):
        vec = [
            float(vector[0]) * value,
            float(vector[1]) * value,
            float(vector[2]) * value]
        return vec


    def vector_unitize(self, vector):
        length = math.sqrt(
            math.pow(float(vector[0]), 2) + 
            math.pow(float(vector[1]), 2) + 
            math.pow(float(vector[2]), 2))
        new_vector = self.vector_multiplicate(vector, (1.0/length))
        return new_vector


    def move_pt_vec(self, pt, vec):
        p = [
            float(pt[0]) + float(vec[0]),
            float(pt[1]) + float(vec[1]),
            float(pt[2]) + float(vec[2])]
        return p


    def face_normal(self, p0, p1, p2):
        v1 = self.pt_pt_subtract(p1, p0)
        v2 = self.pt_pt_subtract(p2, p0)

        # ベクトル同士の外積
        n0 = v1[1] * v2[2] - v1[2] * v2[1]
        n1 = v1[2] * v2[0] - v1[0] * v2[2]
        n2 = v1[0] * v2[1] - v1[1] * v2[0]

        n = (n0, n1, n2)

        return n


    def point_vector_mask(self, list_pvm):

        pp = []
        vv = []
        mm = []

        for i in range(len(list_pvm)):

            pvm = list_pvm[i]
            p_v_m = pvm.split(',')
            # print(p_v_m)
            p = [p_v_m[0], p_v_m[1], p_v_m[2]]
            v = [p_v_m[3], p_v_m[4], p_v_m[5]]
            m = p_v_m[6]

            ### Unitize Vector
            v = self.vector_unitize(v)

            pp.append(p)
            vv.append(v)
            mm.append(m)

        return pp, vv, mm