import sys,os,stat
# #文件夹创建操作
# try:
#     os.mkdir("./mkdir",644,)
#     print(os.listdir())
# except FileExistsError:
#     print("文件夹以存在")

# print("完成")

# a=10
# b=0
# try:
#     c=a/b
#     print (c)
# except ZeroDivisionError:
#     print("异常")
# print ("done")



##文件夹重命名

# os.rename("./mkdir","mkdir1")


#----------------------------------------------------------------查看是文件还是目录


# import sys,os,stat


# def listor(path):
#     files = os.listdir(path)
#     for name in files:
#         filesname = os.path.join(path,name)
#         mode =  os.stat(filesname).st_mode
#         if  stat.S_ISDIR(mode):
#             print("%s 是目录"%filesname)
#         elif stat.S_ISREG(mode):
#             print("%s是文件"%filesname)
#         else:
#             print("无法识别")



# listor("C:\\Users\\Administrator\\Desktop\\xls")


# 其他类型的判断如下：

# if stat.S_ISREG(mode):           #判断是否一般文件
#    print 'Regular file.'
# elif stat.S_ISLNK (mode):         #判断是否链接文件
#    print 'Shortcut.'
# elif stat.S_ISSOCK (mode):        #判断是否套接字文件    
#    print 'Socket.'
# elif stat.S_ISFIFO (mode):        #判断是否命名管道
#    print 'Named pipe.'
# elif stat.S_ISBLK (mode):         #判断是否块设备
#    print 'Block special device.'
# elif stat.S_ISCHR (mode):         #判断是否字符设置
# 　　print 'Character special device.'
# elif stat.S_ISDIR (mode):         #判断是否目录
# 　　print 'directory.'

#---------------------------------------------------------------------------------------




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@创建目录


def  mkdpath(pathname,mode):
        try:
            os.makedirs(pathname,mode)
        except OSError as  e:
            print("目录已存在",e)
        else:
            print("创建成功")

mkdpath('./a/',644)








