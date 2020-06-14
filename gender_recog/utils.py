import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import os

#load model
# model_path = os.path.join(os.getcwd(),'cnn2_acc96_val_88.h5')
# print(model_path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(os.path.join(os.path.join(BASE_DIR,'gender_recog'),'ml_models'),'cnn2_acc96_val_88.h5')

gen_recog_model = tf.keras.models.load_model(model_path)

def pred_gender(path):
    img = image.load_img(path,target_size=(150,150))
    inp_img = image.img_to_array(img)
    inp_img = np.expand_dims(inp_img, axis=0)
    result = gen_recog_model.predict(inp_img)
    print(result[0])
    if result[0]>0.5:
        return 'male'
    else:
        return 'female'
