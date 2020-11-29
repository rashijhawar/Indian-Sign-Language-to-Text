import cv2
import numpy as np

def image_processing(image):
    # Convert from BGR to Grayscale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert from BGR to HSV
    HSVImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

    # Finding pixels with itensity of skin
    lowerBoundary = np.array([0,40,30], dtype="uint8")
    upperBoundary = np.array([43,255,254], dtype="uint8")
    skinMask = cv2.inRange(HSVImage, lowerBoundary, upperBoundary)
    
    # Blurring of gray scale using medianBlur
    skinMask = cv2.addWeighted(skinMask, 0.5, skinMask, 0.5, 0.0)
    skinMask = cv2.medianBlur(skinMask, 5)
    skin = cv2.bitwise_and(grayImage, grayImage, mask = skinMask)
    
    # Canny edge detection
    canny = cv2.Canny(skin, 60, 60)

    #cv2.imshow('', HSVImage)
    #cv2.waitKey(0)

    return canny