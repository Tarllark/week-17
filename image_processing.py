###############################################
#
# Title:	image_processing.py
#
# Descr:	Downloads image of given URL and creates a negative copy.
#
# Author:	Tarllark
#
# Team:		Successful Story
#
###############################################

from webget import download as wget
import cv2 as cv

def image_prep(url='https://i2.wp.com/hennesseyperformance.com/wp-content/uploads/2017/10/6X6-Hennessey-Velociraptor-06.jpg'):
	image = wget(url)
	return cv.imread(image)
	
if __name__ == '__main__':
	cv.imwrite("negative_copy.jpg", cv.bitwise_not(image_prep()))