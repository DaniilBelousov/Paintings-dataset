import os


# Создание директорий для картин классов


def createDirs(root, dirNames):
    # print("joined createDirs()")
    os.chdir(root)
    if not os.path.exists("paintings"):
        os.mkdir("paintings")
    if not os.path.exists("changedPaintings"):
        os.mkdir("changedPaintings")
    path = os.path.join(root, "paintings")
    os.chdir(path)
    for directory in dirNames:
        if not os.path.exists(directory):
            os.mkdir(directory)
            print("Directory created: ", os.path.join(path, directory))
    path = os.path.join(root, "changedPaintings")
    os.chdir(path)
    for directory in dirNames:
        if not os.path.exists(directory):
            os.mkdir(directory)
            print("Directory created: ", os.path.join(path, directory))


if __name__ == "__main__":
    # сюда пихать нозвания новых папок,если их надо создать, иначе оставлять
    # пустым
    dirNames = ("monaLisa", "bearsInTheForest", "theCreationOfAdam")
    # Создаем директории, если их нет
    if len(dirNames) != 0:
        createDirs(os.path.abspath("."), dirNames)
