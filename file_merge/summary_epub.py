# coding:utf-8

import os
import os.path

# 1. 获取要重命名的文件夹 名字
fo1 = "123/"

# 2. 获取制定的文件夹中的所有 文件名字
# names = os.listdir(fo1)
# names.sort()
# print(names)


# for fo in names:
#     try:
#         fo2 = fo1 + fo
#         names2 = os.listdir(fo2)
#         for file in names2:
#             print(file)
#             if file[-2:] == "py":
#                 with open(fo2 + "/" + file) as f:
#                     s = f.read()
#                 with open("book.txt", "a") as ff:
#                     ff.write("**********************************")
#                     ff.write("\n" + fo + "title：" + file[:-3] + "\n" + s + "\n")
#     except Exception as e:
#         print(e)


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile


fileNames = dirlist(fo1, [])
fileNames.sort()


def Merge(files):
    for file in files:
        if file[-2:] == "py":
            with open(file) as f:
                s = f.read()
            with open("python_book.txt", "a") as ff:
                ff.write("**********************************")
                ff.write("\n" + file[:-3] + "\n" + s + "\n")


Merge(fileNames)
