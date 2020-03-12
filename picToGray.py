import cv2 as cv
import os


# Картинка в серый
def pictureToGray(root, pics):
    os.chdir(root)
    for pic in pics:
        gray = cv.imread(pic, 0)
        cv.imwrite(pic, gray)
    print("Directory: ", root)
    print("Changed into gray --> Success")
