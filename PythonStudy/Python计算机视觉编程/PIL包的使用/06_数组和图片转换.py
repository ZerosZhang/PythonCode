import PIL.Image
import numpy as np
from PIL import Image

from 项目 import Tools as logging

img_path = '../../../Data/image/Lenna.jpg'
pil_im: PIL.Image.Image = Image.open(img_path)
# pil_im.show()
logging.warning('跳过原图片的显示...')

im_array = np.array(pil_im)
print(f'原图shape：{im_array.shape}，数据类型{im_array.dtype}')

im_array_L = np.array(pil_im.convert('L'))
print(f'灰度图shape：{im_array_L.shape}，数据类型{im_array_L.dtype}')

pil_im_from_array = Image.fromarray(im_array_L)
pil_im_from_array.show()
# logging.warning('跳过数组转图片的显示...')
