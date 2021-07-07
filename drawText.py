#-*- coding: utf-8 -*-
import PIL.Image as Image
import PIL.ImageColor as ImageColor
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

#设置字体（LiberationSans-Regular.ttf这是我ubuntu16.04自带的字体)
# font = ImageFont.truetype('LiberationSans-Regular.ttf', 60)

#打开图片
imageFile = "xly.jpg"
im1=Image.open(imageFile)

# 在图片上添加文字 1
draw = ImageDraw.Draw(im1)

# (0,0):坐标 "XUNALOVE"：添加的字体 (0,0,255):字体颜色 font:字体大小
draw.text((0, 0),"XUNALOVE",(0,0,255),font=font)
draw = ImageDraw.Draw(im1)

# 保存
im1.save("result.jpg")
