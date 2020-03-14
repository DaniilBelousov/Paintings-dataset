import os
import numpy as np
import cv2 as cv
from albumentations import (
    HorizontalFlip, IAAPerspective, ShiftScaleRotate, CLAHE, RandomRotate90,
    Transpose, ShiftScaleRotate, Blur, OpticalDistortion, GridDistortion, HueSaturationValue,
    IAAAdditiveGaussianNoise, GaussNoise, MotionBlur, MedianBlur, RandomBrightnessContrast, IAAPiecewiseAffine,
    IAASharpen, IAAEmboss, Flip, OneOf, Compose
)
# from main import returnPics


def readImage(pic):
    print("joined readImage()")
    image = cv.imread(pic, cv.IMREAD_UNCHANGED)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    return image


def strong_aug(p=.5):
    print("joined strong_aug()")
    return Compose([
        RandomRotate90(),
        Flip(),
        Transpose(),
        OneOf([
            IAAAdditiveGaussianNoise(),
            GaussNoise(),
        ], p=0.2),
        OneOf([
            MotionBlur(p=.2),
            MedianBlur(blur_limit=3, p=0.1),
            Blur(blur_limit=3, p=0.1),
        ], p=0.2),
        ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2,
                         rotate_limit=45, p=0.2),
        OneOf([
            OpticalDistortion(p=0.3),
            GridDistortion(p=.1),
            IAAPiecewiseAffine(p=0.3),
        ], p=0.2),
        OneOf([
            CLAHE(clip_limit=2),
            IAASharpen(),
            IAAEmboss(),
            RandomBrightnessContrast(),
        ], p=0.3),
        HueSaturationValue(p=0.3),
    ], p=p)


def argment_and_write(aug, image, index, name="pic_", picFormat=".jpg"):
    print("joined argment_and_write()")
    image = aug(image=image)["image"]
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    imageName = name + str(index) + picFormat
    cv.imwrite(imageName, image)


def processImages(root, pics):
    print("joined processImages()")
    index = len(pics)
    os.chdir(root)
    for pic in pics:
        image = readImage(pic)
        for i in range(5):
            aug = strong_aug(p=1)
            argment_and_write(aug, image, index)
            index += 1


# if __name__ == "__main__":
#     path = os.path.join(os.path.abspath("changedPaintings"), "monaLisa")
#     pics = returnPics(path)
#     processImages(path, pics)
