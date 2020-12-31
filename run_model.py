import sys
import tensorflow as tf
from keras.applications.vgg16 import VGG16
import cv2
import math
import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import resize
from keras.applications.vgg16 import preprocess_input


def run_model(file_name):
	video = file_name
	model = tf.keras.models.load_model('trumpbiden_model_final.h5')
	base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))    # include_top=False to remove the top layer

	count = 0
	videoFile = file_name
	cap = cv2.VideoCapture(videoFile)
	frameRate = cap.get(5) #frame rate
	x=1
	while(cap.isOpened()):
	    frameId = cap.get(1) #current frame number
	    ret, frame = cap.read()
	    if (ret != True):
	        break
	    if (frameId % math.floor(frameRate) == 0):
	        filename ="test_imgs/testtrump%d.jpg" % count;count+=1
	        cv2.imwrite(filename, frame)
	cap.release()



	test_imagenames = os.listdir("test_imgs")


	test_image = []
	for img_name in test_imagenames:
	    img = plt.imread('' + img_name)
	    test_image.append(img)
	test_img = np.array(test_image)

	test_image = []
	for i in range(0,test_img.shape[0]):
	    a = resize(test_img[i], preserve_range=True, output_shape=(224,224)).astype(int)
	    test_image.append(a)
	test_image = np.array(test_image)
	# preprocessing the images
	test_image = preprocess_input(test_image)

	# extracting features from the images using pretrained model
	test_image = base_model.predict(test_image)

	predictions = model.predict_classes(test_image)
	print("====================Prediction: ", predictions," ==================")
	if 1 in predictions:
		print("====================Trump is in this video==================")


if __name__ == '__main__':
	if len(sys.argv) == 1:
	    print("Error: trending video did not download please try again")

	else:
	    filename = sys.argv[1]
	    run_model(filename)
