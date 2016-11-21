# -*- coding: utf-8 -*-
import os
from PIL import Image

cdir = os.path.abspath('.') + "/"

def get_feature(img):
    width, height = img.size
    pixel_cnt_list = []
    height = 13 #一个数字的高度是13个像素点
    for y in range(height):
        pix_cnt_x = 0
        for x in range(width):
            if img.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_x += 1
        pixel_cnt_list.append(pix_cnt_x)
    for x in range(width):
        pix_cnt_y = 0
        for y in range(height):
            if img.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_y += 1
        pixel_cnt_list.append(pix_cnt_y)
    return pixel_cnt_list


def genTxt():
    pixtxt = file(cdir + 'test.txt', 'wb')
    line = ''
    for d in range(1):
        dir1 = cdir + "cutRes"
        print dir1
        trainCount = 0
        for parent, dirnames, filenames in os.walk(dir1):
            print parent, dirnames, filenames
            for filename in filenames:
                if trainCount + 1 > 8:
                    pass
                else:
                    img_path = dir1 + '/' + filename
                    im = Image.open(img_path)
                    pixels = get_feature(im)
                    line = str(d)
                    index = 0
                    for px in pixels:
                        index = index + 1
                        line = line + " " + str(index) + ":" + str(px)
                    print line
                    pixtxt.write(line + "\n")

    pixtxt.close()
    # 就将图片素材特征化，按照 libSVM 指定的格式生成一组带特征值和标记值的向量文件


if __name__ == "__main__":
    genTxt()


