import os
import cv2 as cv


# Изменение размера картинки
# scalePercent - процент от оригинального изображения - параметр убран
# calePercent
def resizePic(root, exportPath, pics, width, height):
    # os.chdir(root)
    # picPath_0 = pics[0]
    # img_0 = cv.imread(picPath_0, cv.IMREAD_UNCHANGED)
    # width = int(img_0.shape[1] * scalePercent / 100)
    # height = int(img_0.shape[0] * scalePercent / 100)
    for pic in pics:
        os.chdir(root)
        img = cv.imread(pic, cv.IMREAD_UNCHANGED)
        print("Original Dimensions " + pic + " : ", img.shape)
        dim = (width, height)
        # resize image
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        print("Resized Dimensions " + pic + " : ", resized.shape)
        # print("Before saving image:")
        # print(os.listdir(root))
        os.chdir(exportPath)
        cv.imwrite(pic, resized)
    print("Directory ", root)
    print("Resize --> Success")
