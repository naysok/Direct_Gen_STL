#########################################################
### Utilities                                         ###
###                                                   ###
###                                                   ###
#########################################################



class UTIL():


    def pt_pt_subtract(self, pt0, pt1):
        pt = (pt1[0] - pt0[0], pt1[1] - pt0[1], pt1[2] - pt0[2])
        return pt


    def move_pt_vec(self, pt, vec):
        xx = pt[0] + vec[0]
        yy = pt[1] + vec[1]
        zz = pt[2] + vec[2]
        p = [xx, yy, zz]
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


    def remap_number(self, src, old_min, old_max, new_min, new_max):
        return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)

    
    def point_vector_mask(self, list_pvm):

        pp = []
        vv = []
        mm = []

        for i in range(len(list_pvm)):

            pvm = list_pvm[i]
            p_v_m = pvm.split(',')
            p = [p_v_m[0], p_v_m[1], p_v_m[2]]
            v = [p_v_m[3], p_v_m[4], p_v_m[5]]
            m = p_v_m[6]

            pp.append(p)
            vv.append(v)
            mm.append(m)

        return pp, vv, mm