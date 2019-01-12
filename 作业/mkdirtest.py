import os
##创建目录
# def  mkdpath(pathname,mode):
#         try:
#             os.makedirs(pathname,mode)
#         except OSError as  e:
#             print("目录已存在",e)
#         else:
#             print("创建成功")

# mkdpath('./a/',644)

## 判断目录是否存在


def mkdpath(pathname,mode):
    if not os.path.exists(pathname):
        os.makedirs(p,mode)
    else:
        print("目录已存在")
    print("done")


mkdpath("./a",644)
