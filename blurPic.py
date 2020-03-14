import os
import cv2 as cv


# Блюр картинок
def blurPicture(root, pics, kernels, picFormat=".jpg"):
    os.chdir(root)
    index = len(pics)
    for pic in pics:
        img = cv.imread(pic, cv.IMREAD_UNCHANGED)
        blured = cv.blur(img, kernels)
        newName = "pic_" + str(index) + picFormat
        cv.imwrite(newName, blured)
        index += 1
    print("Directory: ", root)
    print("Blur --> Success")
