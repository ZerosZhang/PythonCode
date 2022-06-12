import PIL.Image
from PIL import Image

from 项目 import Tools as logging

img_path = '../../../Data/image/Lenna.jpg'
pil_im: PIL.Image.Image = Image.open(img_path)
# pil_im.show()
logging.warning('跳过原图片的显示...')

# 图像格式
"""
==============================================================
1：1位像素，表示黑和白，但是存储的时候每个像素存储为8bit
L：8位像素，表示黑和白
P：8位像素，使用调色板映射到其他模式
RGB：3x8位像素，为真彩色
RGBA：4x8位像素，有透明通道的真彩色
CMYK：4x8位像素，颜色分离
YCbCr：3x8位像素，彩色视频格式
I：32位整型像素
F：32位浮点型像素
"""
logging.info(f'原图的格式为【{pil_im.mode}】')
pil_im_gray = pil_im.convert('L')
logging.info(f'转换后的格式为【{pil_im_gray.mode}】')
# pil_im_gray.show()
logging.warning('跳过图片灰度化的显示...')
