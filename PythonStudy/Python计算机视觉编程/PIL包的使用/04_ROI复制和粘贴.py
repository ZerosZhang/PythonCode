import PIL.Image
from PIL import Image

from 项目 import Tools as logging

img_path = '../../../Data/image/Lenna.jpg'
pil_im: PIL.Image.Image = Image.open(img_path)
# pil_im.show()
logging.warning('跳过原图片的显示...')

# 复制和粘贴图像区域
box = (0, 0, 400, 400)
region = pil_im.crop(box)
logging.info(f'图片复制操作...')
# region.show()
logging.warning('跳过图片复制的显示...')

region = region.transpose(Image.ROTATE_180)
logging.info(f'复制区域【逆时针】旋转180度...')
pil_im_paste = pil_im.copy()
pil_im_paste.paste(region, box)
logging.info(f'图片粘贴操作...')
# pil_im_paste.show()
logging.warning('跳过图片粘贴的显示...')
