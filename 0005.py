from PIL import Image
import os

path = 'D:/Pyhton学习/img'  #照片目录
resultPath = 'D:/Pyhton学习/result'  #修改后的结果目录
if not os.path.isdir(resultPath): #判断是否为一个文件
    os.mkdir(resultPath)       #创建一个文件
for picName in os.listdir(path):  #当照片属于指定文件夹
    picPath = os.path.join(path, picName) #将路径和名称拼接在一起成为一个新路径
    print(picPath)
    with Image.open(picPath) as im:
        w, h = im.size
        n = w / 1366 if (w / 1136) >= (h / 640) else h / 640 #确定缩小倍数
        im.thumbnail((w / n, h / n))  #缩小照片尺寸n倍
        im.save(resultPath+'/finish_' + picName.split('.')[0] + '.jpg', 'jpeg')
