# -*- coding: utf-8 -*-
import os

from PIL import Image

cdir = os.path.abspath('.') + "/"

def cut():
    for k in range(1):
        img_path = cdir + "pictures/gres" + str(k) + ".jpg"
        im = Image.open(img_path)
        for i in range(4):
            x = 7 + i * (8 + 5)  #第一个字的像素从第8列开始，第个字横向占8个像素点，第两个字横向间隔5个像素点
            y = 3 #从第二行开始，一个数的像素点是8列,13行
            child_img = im.crop((x, y, x + 8, y + 13))
            if not os.path.exists(cdir + "cutRes"):
                os.mkdir(cdir+"cutRes")
            child_img.save(cdir+"cutRes/" +str(i)+'.jpg')