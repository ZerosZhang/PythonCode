import PIL.Image
from PIL import Image

from 项目 import Tools as logging

img_path = '../../../Data/image/Lenna.jpg'
pil_im: PIL.Image.Image = Image.open(img_path)
# pil_im.show()
logging.warning('跳过原图片的显示...')

# 缩略图
pil_im_thumbnail = pil_im.copy()
pil_im_thumbnail.thumbnail((128, 128))
# pil_im_thumbnail.show()
logging.warning('跳过图片缩略的显示...')
