# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:23:06 2020

@author: 79167
"""
import shutil
import os                #遍历文件夹
# 复制图像到另一个文件夹
# 文件所在文件夹
file_dir = 'D:\zhaop2'
# 创建一个子文件存放文件
name = 'chosen'

file_list = os.listdir(file_dir)
i=1
for image in file_list:
#    print(image)
    filenames = os.listdir(os.path.join(file_dir,image))
    b=os.path.join(file_dir,'class_name')
#    print(b)
    #如果图像名为B.png 则将B.png复制到F:\\Test\\TestA\\class
#    print(filenames)
    for image1 in filenames:
        if image1 == "119.png":
#            print(1)
            if os.path.exists(os.path.join(file_dir,'class_name')):
                new_path = os.path.join(file_dir,'class_name')
                new_image = new_path + '/' + str(i) + '.png'
#                print(new_image)
                a=os.path.join(os.path.join(file_dir,image),str(image1))
                print(a)
                print(new_image)
                shutil.copyfile(a,new_image)
                i=i+1
