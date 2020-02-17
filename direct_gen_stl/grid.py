import math

from . import util



class Grid():


    def gen_grid(self, count):

        grid = []

        for i in range(count):
            sub = []
            for j in range(count):
                p = (i, j, 0)
                sub.append(p)
            grid.append(sub)
        
        return grid


    def gen_grid_sin(self, count):

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



    def gen_grid_image(self, count, colors, amp):

        ut = util.UTIL()

        grid = []

        if len(colors[0][0]) == 3:
            for i in range(count):
                sub = []
                for j in range(count):

                    ### COLOR CHANNEL
                    RR, GG, BB = colors[i][j]
                    RR = ut.remap_number(RR, 0, 255, 0, amp)
                    p = (i, j, RR)
                    sub.append(p)
                grid.append(sub)
            
        if len(colors[0][0]) == 4:
            for i in range(count):
                sub = []
                for j in range(count):

                    ### COLOR CHANNEL
                    RR, GG, BB, AA = colors[i][j]
                    RR = ut.remap_number(RR, 0, 255, 0, amp)
                    p = (i, j, RR)
                    sub.append(p)
                grid.append(sub)
        
        return grid


    def gen_grid_cylinder(self, count, rad):

        grid = []

        for i in range(counts):
            sub_g = []
            for j in range(count):

                p = 
                center_length = math.sqrt(math.pow((i - center[0]), 2) + math.pow((j - center[0]), 2)) 
                z = math.cos(ut.remap_number(center_length, 0, count, 0, math.pi))
                p = (i, j, z * amp)


                sub_g.append(p)
            grid.append(sub_g)
        
        return grid


    def gen_grid_image_volume(self, count, colors, amp):

        ut = util.UTIL()

        modify_z = 5

        grid_top = []
        grid_bottom = []

        if len(colors[0][0]) == 3:
            for i in range(count):
                sub_top = []
                sub_bottom = []
                for j in range(count):

                    ### COLOR CHANNEL
                    RR, GG, BB = colors[i][j]
                    RR = ut.remap_number(RR, 0, 255, 0, amp)

                    p_top = (i, j, RR + modify_z)
                    p_bottom = (i, j, RR - modify_z)

                    sub_top.append(p_top)
                    sub_bottom.append(p_bottom)

                grid_top.append(sub_top)
                grid_bottom.append(sub_bottom)

            
        if len(colors[0][0]) == 4:
            for i in range(count):
                sub_top = []
                sub_bottom = []

                for j in range(count):

                    ### COLOR CHANNEL
                    RR, GG, BB, AA = colors[i][j]
                    RR = ut.remap_number(RR, 0, 255, 0, amp)

                    p_top = (i, j, RR + modify_z)
                    p_bottom = (i, j, RR + modify_z)

                    sub_top.append(p)
                    sub_bottom.append(p)

                grid_top.append(sub_top)
                grid_bottom.append(sub_bottom)
        

    
        return grid



    def seg_pt4(self, grid):

        pt4s = []

        for u in range(len(grid) - 1):
            for v in range(len(grid[0]) - 1):
                pt4 = []

                pt4.append(grid[u][v])
                pt4.append(grid[u+1][v])
                pt4.append(grid[u][v+1])
                pt4.append(grid[u+1][v+1])

                pt4s.append(pt4)

        return pt4s
    

    def seg_pt4_masking(self, grid, mask_grid):

        pt4s = []

        for u in range(len(grid) - 1):
            for v in range(len(grid[0]) - 1):
                
                # print("UV", u, v)
                
                mask_tf = mask_grid[u][v]

                if mask_tf == 1:
                    pt4 = []

                    pt4.append(grid[u][v])
                    pt4.append(grid[u+1][v])
                    pt4.append(grid[u][v+1])
                    pt4.append(grid[u+1][v+1])

                    pt4s.append(pt4)

        return pt4s
