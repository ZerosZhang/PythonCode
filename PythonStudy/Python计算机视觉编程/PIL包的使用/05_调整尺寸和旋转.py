import PIL.Image
from PIL import Image

from 项目 import Tools as logging

img_path = '../../../Data/image/Lenna.jpg'
pil_im: PIL.Image.Image = Image.open(img_path)
# pil_im.show()
logging.warning('跳过原图片的显示...')

pil_im_resize = pil_im.resize((128, 128))
# pil_im_resize.show()
logging.warning('跳过图片调整大小的显示...')

pil_im_rotate = pil_im.rotate(45)
# pil_im_rotate.show()
logging.warning('跳过图片旋转的显示...')
