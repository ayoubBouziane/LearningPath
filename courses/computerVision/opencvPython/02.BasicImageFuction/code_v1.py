# Will learn cv2.imread, cv2.namedWindow, cv2.imshow, cv2.imwrite, cv2.waitKey and cv2.distroyAllWindow
# using waitKey to take a decision based on user Input
import numpy as np  #Import Numpy Package
import cv2          #Import opencv Package

#Load an image without change in pixel
img_color = cv2.imread('../Image/testImage.jpeg', cv2.IMREAD_UNCHANGED)
#Load an color image in grayscale
img_gray = cv2.imread('../Image/testImage.jpeg', cv2.IMREAD_GRAYSCALE)

#keyboard binding function
k = cv2.waitKey(0) & 0xFF

if k == 27: # Wait for ESC Key to exit
    #simply destroys all the windows we created.
    cv2.distroyAllWindow()
elif k == ord('s'): #Wait for S to show the image on Windows
    # Creates a window
    cv2.namedWindow('Test_Image_Color',cv2.WINDOW_AUTOSIZE)
    # Load the new image on Opencv Windows
    cv2.imshow('Test_Image_Color', img_color)

    # Creates a window
    cv2.namedWindow('Test_Image_Gray ',cv2.WINDOW_AUTOSIZE)
    # Load the new image on Opencv Window
    cv2.imshow('Test_Image_Gray', img_gray)
elif k == ord('w'): #Wait for w to write an image
    #Save the grayscale image into new file
    cv2.imwrite('Test_Image_Gray.jpeg', img_gray)
