#-*- coding: utf-8 -*-
import cv2
import numpy as np
import keras.models

import digit_detector.region_proposal as rp
import digit_detector.show as show
import digit_detector.detect as detector
import digit_detector.file_io as file_io
import digit_detector.preprocess as preproc
import digit_detector.classify as cls

detect_model = "detector_model.hdf5"
recognize_model = "recognize_model.hdf5"

mean_value_for_detector = 107.524
mean_value_for_recognizer = 112.833

model_input_shape = (32,32,1)
#DIR = '../datasets/svhn/train'
DIR = '../datasets'

if __name__ == "__main__":
    # 1. image files
    img_files = file_io.list_files(directory=DIR, pattern="*.png", recursive_option=False, n_files_to_sample=4, random_order=False)

    preproc_for_detector = preproc.GrayImgPreprocessor(mean_value_for_detector)
    preproc_for_recognizer = preproc.GrayImgPreprocessor(mean_value_for_recognizer)

    char_detector = cls.CnnClassifier(detect_model, preproc_for_detector, model_input_shape)
    char_recognizer = cls.CnnClassifier(recognize_model, preproc_for_recognizer, model_input_shape)
    
    digit_spotter = detector.DigitSpotter(char_detector, char_recognizer, rp.MserRegionProposer())
    
    for img_file in img_files[0:]:
        # 2. image
        img = cv2.imread(img_file)

        # ORIGINAL
        #digit_spotter.run(img, threshold=0.5, do_nms=True, nms_threshold=0.1)

        # Think it gets rid of some false positives
        #digit_spotter.run(img, threshold=0.7, do_nms=True, nms_threshold=0.1)

        # get's rid of alot of false positives.
        #digit_spotter.run(img, threshold=0.9, do_nms=True, nms_threshold=0.1)

        # get's rid of alot of false positives.
        # This one seems pretty good for the initial test image,
        # with a corresponding text classifier then we could be onto something.
        digit_spotter.run(img, threshold=0.95, do_nms=True, nms_threshold=0.1)







