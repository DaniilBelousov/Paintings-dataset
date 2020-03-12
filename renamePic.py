import os

# Изменение названия избражений на pic_0 pic_1 и тд


def renamePictures(root, pics, name="pic"):
    index = 0
    for pic in pics:
        picPath = root + "\\" + pic
        newName = root + "\\" + name + "_" + str(index) + ".png"
        os.rename(picPath, newName)
        index += 1
    print("Directory ", root)
    print("File rename --> Success")
