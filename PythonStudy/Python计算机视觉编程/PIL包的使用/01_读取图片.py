import os

import PIL.Image
from PIL import Image

from 项目 import Tools as logging

img_path = '../../../Data/image/Lenna.jpg'
img_name = os.path.basename(img_path)
logging.info(f'读取图片【{img_name}】...')
pil_im: PIL.Image.Image = Image.open(img_path)
logging.info(f'图片尺寸【{pil_im.size}】...')
# pil_im.show()
logging.warning('跳过原图片的显示...')
