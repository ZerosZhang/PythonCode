import PIL.Image
import numpy as np
from PIL import Image
from scipy.ndimage import filters

from 项目 import Tools as logging

img_path = '../../../../Data/image/Lenna.jpg'
pil_im: PIL.Image.Image = Image.open(img_path)
# pil_im.show()
logging.warning('跳过原图片的显示...')

im_array = np.array(pil_im.convert('L'))
im_filter = filters.gaussian_filter(im_array, 5)

pil_im_from_array = Image.fromarray(im_filter)
pil_im_from_array.show()
# logging.warning('跳过图片高斯滤波的显示...')
