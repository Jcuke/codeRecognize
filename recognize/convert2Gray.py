# -*- coding: utf-8 -*-
import os

import Image
# 将RGB彩图转为灰度图
# 将灰度图按照设定阈值转化为二值图

cpath = os.path.abspath('.')
rpath = cpath + "/pictures/"

def getGrayPic():
    for i in range(1):
        convertResPicPath = rpath + 'g'+ str(i) +'.jpg'
        convertResPicPath2 = rpath + 'gres' + str(i) + '.jpg'
        img_path = rpath+ str(i) +".jpg"
        image = Image.open(img_path)
        imgry = image.convert('L')  # 转化为灰度图
        imgry.save(convertResPicPath)
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        #灰度二值化，保存黑白两色
        bim = imgry.point(table, '1')
        bim.save(convertResPicPath2)

