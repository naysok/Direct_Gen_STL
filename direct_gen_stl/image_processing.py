import math
from PIL import Image, ImageDraw

from . import util



class ImageProcessing():


    def get_color_to_memory(self, path):

        img = Image.open(path)

        size = img.size

        cl_l = []

        for i in range(size[1]):

            cl = []

            for j in range(size[0]):
                c = img.getpixel((j, i))
                cl.append(c)
            
            cl_l.append(cl)
        
        return cl_l


    def get_mask(self, path, threshold):

        img = Image.open(path)

        size = img.size

        mask = []

        for i in range(size[1]):

            sub = []

            for j in range(size[0]):
                
                c = img.getpixel((j, i))
                value = c[0]

                ### null
                if value >> threshold:
                    sub.append(1)
                    # print("1")
                
                ### masked
                else:
                    sub.append(0)
                    # print("0")

            
            mask.append(sub)
        
        return mask


