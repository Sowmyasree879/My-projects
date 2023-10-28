# -*- coding: utf-8 -*-
# Author: yongyuan.name

import numpy as np
from numpy import linalg as LA
import tensorflow as tf

import keras.models
from keras.models import load_model

import tensorflow_io as tfio

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

class CustomModel:
    def __init__(self):
        self.input_shape = (224,224,3)
        self.model = load_model('vgg16_1.h5')
       # self.model.predict(np.zeros(224,224,3))

    def extract_feat(self, img_path):
        #image_bytes = tf.io.read_file(img_path)
        #img = tfio.image.decode_dicom_image(image_bytes, dtype=tf.uint16)
        img = image.load_img(img_path, target_size=(self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        norm_feat = feat[0]/LA.norm(feat[0])
        return norm_feat
    


class VGGNet:
    def __init__(self):
        # weights: 'imagenet'
        # pooling: 'max' or 'avg'
        # input_shape: (width, height, 3), width and height should >= 48
        self.input_shape = (224, 224, 3)
        self.weight = 'imagenet'
        self.pooling = 'max'
        self.model = VGG16(weights = self.weight, input_shape = (self.input_shape[0], self.input_shape[1], self.input_shape[2]), pooling = self.pooling, include_top = False)
        self.model.predict(np.zeros((1, 224, 224 , 3)))
        

    '''
    Use vgg16 model to extract features
    Output normalized feature vector
    '''
    def extract_feat(self, img_path):
        #image_bytes = tf.io.read_file(img_path)
        #img = tfio.image.decode_dicom_image(image_bytes, dtype=tf.uint16)
        img = image.load_img(img_path, target_size=(self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        norm_feat = feat[0]/LA.norm(feat[0])
        return norm_feat




#image = tfio.image.decode_dicom_image(image_bytes, dtype=tf.uint16)
