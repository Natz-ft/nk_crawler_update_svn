import numpy as np
import string
from tensorflow.keras.models import load_model
import tensorflow.keras.backend as K
import cv2 as cv
from PIL import Image

characters = string.digits + string.ascii_uppercase + string.ascii_lowercase


def captcha_1_pred(img, model):

    base_model = model

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    im = cv.resize(gray, (120, 40), interpolation=cv.INTER_AREA) / 255.0

    y_pred = base_model.predict(im.reshape((-1, 40, 120, 1)))
    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]

    li = [characters[x] for x in out[0]]
    res = ''.join(li)

    return res


if __name__ == '__main__':
    i = 93
    res = captcha_pred(r'./test\{}_img.jpg'.format(i), 'model_1.h5')
    print(res)