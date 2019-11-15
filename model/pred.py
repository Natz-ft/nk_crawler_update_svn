import numpy as np
import string
from tensorflow.keras.models import load_model
import tensorflow.keras.backend as K
import cv2 as cv
from PIL import Image


#bidchance.com
def captcha_1_pred(img, model):
    characters = string.digits + string.ascii_uppercase + string.ascii_lowercase
    
    base_model = model

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    im = cv.resize(gray, (120, 40), interpolation=cv.INTER_AREA) / 255.0

    y_pred = base_model.predict(im.reshape((-1, 40, 120, 1)))
    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]

    li = [characters[x] for x in out[0]]
    res = ''.join(li)

    return res

#okcis.cn
def captcha_2_pred(img, model):

    characters = string.digits + 'x+-=?'

    # base_model = load_model(model_path)
    base_model = model

    # src = cv.imread(img_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    im = cv.resize(gray, (200, 60), interpolation=cv.INTER_AREA) / 255.0

    y_pred = base_model.predict(im.reshape((-1, 60, 200, 1)))
    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :5]

    li = [characters[x] for x in out[0]]
    for i,data in enumerate(li):
        if data == 'x':
            li[i] = '10'

    if li[1] == '+':
        res = int(li[0]) + int(li[2])
    else:
        res = int(li[0]) - int(li[2])

    return res

