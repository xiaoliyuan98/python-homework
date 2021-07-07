from PIL import Image, ImageDraw,ImageFont
import random

num = str(random.randint(1, 99))

imgPath = 'D:/Pyhton学习/xly.jpg'
img = Image.open(imgPath)
w, h = img.size
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("consola.ttf", 50)#设置字体
draw.text([int(0.8*w), int(0.05*h)], str(num), (255, 0, 0), font=font)
img.show()
img.save('result.jpg')