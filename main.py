import os
import numpy as numpy
import cv2 as cv 
from renamePic import renamePictures
from changeResolution import resizePic
from blurPic import blurPicture
from picToGray import pictureToGray
from albumentations import (HueSaturationValue)


# Возвращает пути к файлам с картинками
# dirName - путь к папке с исходными изображениями
# exportDirName - путь к папке с обработанными изображениями
def returnPaths(dirName):
    path = os.path.abspath(dirName)
    for root, dirs, files in os.walk(path):
        return root, dirs

# Возвращает все названия изображений в директории


def returnPics(dirName):
    for root, dirs, files in os.walk(dirName):
        return files

# Создание директорий для картин классов


def createDirs(root, dirNames):
    # print("joined createDirs()")
    path = os.path.abspath(root)
    os.chdir(path)
    for directory in dirNames:
        if not os.path.exists(directory):
            os.mkdir(directory)
            print("Directory created: ", os.path.join(exportRoot, directory))


if __name__ == "__main__":
    # ----------------------------------------------
    # Инициализация папок и путей - лучше не трогать!!
    # путь к папке с исходными изображениями
    dirNames = () # сюда пихать нозвания новых папок,если их надо создать, иначе оставлять пустым
    root, dirs = returnPaths("paintings")                            
    # путь к изображениям, обработанным
    exportRoot, exportDirs = returnPaths("changedPaintings")
    # Создаем директории, если их нет
    if len(dirNames) != 0:
        createDirs(exportRoot, dirNames)
    # Создание путей к папкам с классами
    for i in range(len(dirs)):
        dirs[i] = root + "\\" + dirs[i]
    for i in range(len(exportDirs)):
        exportDirs[i] = exportRoot + "\\" + exportDirs[i]
    #===============================================
    # Инициализация переменных - можно трогать)
    # Для изменения разрешения
    width = 300
    height = 300
    # Для блюра, при увеличении параметров, размытие становится больше
    kernels = (5, 5)
    # ----------------------------------------------
    print("Main root: ", root)
    print("Directories: ", dirs)
    print("Exprot root: ", exportRoot)
    print("Exprot dirs: ", exportDirs)
    # здесь уже выполняется основной код
    for i in range(len(dirs)):
        pics = returnPics(dirs[i])
        # Переименовывает все фотографии в папке | picFormat можно менять
        renamePictures(dirs[i], pics, picFormat=".jpg")
        pics = returnPics(dirs[i])
        # изменить размер фото | width height можно менять
        resizePic(dirs[i], exportDirs[i], pics, width, height)
        # Блюр | kernels можно менять 
        # pics = returnPics(exportDirs[i])
        # blurPicture(exportDirs[i], pics, kernels)
        pics = returnPics(exportDirs[i])
        # Картинки в серые
        pictureToGray(exportDirs[i], pics)
