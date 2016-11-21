import os
from svmutil import svm_read_problem, svm_train, svm_save_model

cdir = os.path.abspath('.') + "/"
def train_svm_model():
    y, x = svm_read_problem(cdir + 'train_pix_feature_xy.txt')
    model = svm_train(y, x)
    print type(model)
    svm_save_model(cdir + 'model', model)

if __name__ == "__main__":
    train_svm_model()