import os
from renamePic import renamePictures
from changeResolution import resizePic
from blurPic import blurPicture
from picToGray import pictureToGray


# Возвращает пути к файлам с картинками
# dirName - путь к папке с исходными изображениями
# exportDirName - путь к папке с обработанными изображениями
def returnPaths(dirName):
    path = os.path.abspath(dirName)
    for root, dirs, files in os.walk(path):
        return root, dirs


def returnPics(dirName):
    for root, dirs, files in os.walk(dirName):
        return files


if __name__ == "__main__":
    # ----------------------------------------------
    #  Инициализация всех необходимых переменных
    # путь к папке с исходными изображениями
    root, dirs = returnPaths("paintings")
    # путь к изображениям, обработанным
    exportRoot, exportDirs = returnPaths("changedPaintings")
    # Для 0 класса
    root_0 = os.path.abspath("paintings_0")
    exportRoot_0 = os.path.abspath("changedPaintings_0")
    # Для изменения разрешения
    # scalePercent = 30
    width = 300
    height = 300
    # Для блюра
    kernels = [(2, 2), (3, 3)]
    # ----------------------------------------------
    print("Main root: ", root)
    print("Directories: ", dirs)
    print("Exprot root: ", exportRoot)
    print("Exprot dirs: ", exportDirs)
    print("Main root_0: ", root_0)
    print("Exprot root_0: ", exportRoot_0)
    # Создание путей к папкам с классами
    for i in range(len(dirs)):
        dirs[i] = root + "\\" + dirs[i]
        # print(dirs[i])
    for i in range(len(exportDirs)):
        exportDirs[i] = exportRoot + "\\" + exportDirs[i]

    for i in range(len(dirs)):
        pics = returnPics(dirs[i])
        renamePictures(dirs[i], pics)
        pics = returnPics(dirs[i])
        resizePic(dirs[i], exportDirs[i], pics, width, height)
        # pics = returnPics(exportDirs[i])
        # blurPicture(exportDirs[i], pics, kernels)
        pics = returnPics(exportDirs[i])
        pictureToGray(exportDirs[i], pics)
    # Обработка 0 класса
    pics_0 = returnPics(root_0)
    renamePictures(root_0, pics_0)
    pics_0 = returnPics(root_0)
    resizePic(root_0, exportRoot_0, pics_0, width, height)
    # pics_0 = returnPics(exportDirs_0[i])
    # blurPicture(exportDirs_0[i], pics_0, kernels_0)
    pics_0 = returnPics(exportRoot_0)
    pictureToGray(exportRoot_0, pics_0)
