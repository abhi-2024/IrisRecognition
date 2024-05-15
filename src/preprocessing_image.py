import cv2
import numpy as np

def preprocess_image(image1, image2):
   
    height = min(image1.shape[0], image2.shape[0])
    width = min(image1.shape[1], image2.shape[1])
    image1 = cv2.resize(image1, (width, height))
    image2 = cv2.resize(image2, (width, height))
    

    gray_scale1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_scale2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


    gray_scale1 = cv2.resize(gray_scale1, (500, 500))
    gray_scale2 = cv2.resize(gray_scale2, (500, 500))

  
    gray_scale1 = cv2.GaussianBlur(gray_scale1, (9, 9), 1)
    gray_scale2 = cv2.GaussianBlur(gray_scale2, (9, 9), 1)


    gray_scale1 = cv2.equalizeHist(gray_scale1)
    gray_scale2 = cv2.equalizeHist(gray_scale2)

 
    kernel = np.ones((5,5),np.uint8)
    gray_scale1 = cv2.morphologyEx(gray_scale1, cv2.MORPH_OPEN, kernel)
    gray_scale2 = cv2.morphologyEx(gray_scale2, cv2.MORPH_OPEN, kernel)

    return gray_scale1, gray_scale2