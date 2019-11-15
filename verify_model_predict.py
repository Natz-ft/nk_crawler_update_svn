# -*- coding: utf-8 -*-
from tensorflow.keras.models import load_model
import os
import sys
sys.path.append(os.path.abspath("./model"))
from pred import captcha_1_pred,captcha_2_pred
import traceback

def getVerifyCode_func(cutImg,modelpath):
    modelPathdic = {"model_1.h5":captcha_1_pred,"model_2.h5":captcha_2_pred}
    model = load_model(os.path.abspath("./model/"+modelpath))
    func = modelPathdic[modelpath]
    try:
        res = func(cutImg,model)
    except Exception as e:
        print('getVerifyCode_func error: ', e)
        traceback.print_exc()
        res = ""
    return res 

class Verify_code_predict:
    def __init__(self):
        self.modelPathdic =  {"model_1.h5":captcha_1_pred,"model_2.h5":captcha_2_pred}
        self.model = {}
        for modelpath in self.modelPathdic.keys():
            self.model[modelpath] = load_model(os.path.abspath("./model/"+modelpath))
    def getVerifyCode(self,cutImg,modelpath):
        modelname = os.path.basename(modelpath)
        if modelname in self.modelPathdic.keys():
            func = self.modelPathdic[modelname]
            item_model = self.model[modelname]
            try:
                res = func(cutImg,item_model)
            except Exception as e:
                print('getVerifyCode error: ', e)
                traceback.print_exc()
                res = ""
            return res
        else:
            print("modelpath not in Verify_code_predict __init__")
            return ""
           
if __name__ == '__main__':
    import cv2
    predict = Verify_code_predict()
    imgPath = "./model/captcha_img.jpg"
    cutImg = cv2.imread(imgPath)
    result = predict.getVerifyCode(cutImg, 'model_1.h5')
    print(result)