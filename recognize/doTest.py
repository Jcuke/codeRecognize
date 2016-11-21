# -*- coding: UTF-8 -*-
import os

import shutil

import time
from svmutil import svm_read_problem, svm_load_model, svm_predict

from recognize.convert2Gray import getGrayPic
from recognize.cut import cut
from recognize.genTxt import genTxt
from recognize.getPic import downloads_pic

cdir = os.path.abspath('.') + "/"
testTxt = cdir + 'test.txt'
modelFile = cdir + "model"


def doRecognize():
    yt, xt = svm_read_problem(testTxt)
    model = svm_load_model(cdir + "model")
    p_label, p_acc, p_val = svm_predict(yt, xt, model)#p_label即为识别的结果
    code = ''
    for item in p_label:
        code = code + str(int(item))
    print code

if __name__ == "__main__":
    shutil.rmtree(cdir + 'cutRes')
    os.mkdir(cdir + 'cutRes')
    shutil.rmtree(cdir + 'pictures')
    os.mkdir(cdir + 'pictures')
    downloads_pic()
    time.sleep(1)
    getGrayPic()
    cut()
    genTxt()
    doRecognize()