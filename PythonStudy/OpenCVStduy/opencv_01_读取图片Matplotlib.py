import cv2
from matplotlib import pyplot as plt

"""
使用Matplotlib库来显示图片，当图片很大的时候这种方式有点卡卡的
"""
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def ImageRead(_path, _flag=cv2.IMREAD_GRAYSCALE):
    """
    封装opencv读取图像  https://www.wolai.com/zeros/t7b5k4dF1d7zdBpN3XhhJz?theme=light
    @param _path: 路径中不能包含中文，支持相对路径和绝对路径
    @param _flag: 读取图片的方式，默认为灰度图
    @return:
    """
    _img = cv2.imread(_path, _flag)
    if _img is None:  # 出错时为None
        print(f"读取图像出错，请检查文件路径")
        return
    print(f"图像【{_path}】尺寸:{_img.shape}")  # 图像尺寸
    return _img


def ImageShowMat(_img, _name="图片", _size=(8, 8)):
    """
    使用matplotlib库来显示图片 https://www.wolai.com/zeros/t7b5k4dF1d7zdBpN3XhhJz?theme=light
    @param _img: 需要显示的图片
    @param _name: 图片的标题，默认为“图片”
    @param _size: 窗口的尺寸，默认为800*800像素
    @return:
    """
    plt.figure(figsize=_size)
    plt.title(_name, fontsize='xx-large')
    plt.xticks([]), plt.yticks([])  # 隐藏刻度值

    if len(_img.shape) == 3:
        _temp = cv2.cvtColor(_img, cv2.COLOR_BGR2RGB)
        plt.imshow(_temp, interpolation='None')
    else:
        plt.imshow(_img, cmap='gray', interpolation='None')
    plt.show()


if __name__ == '__main__':
    m_image = ImageRead(r'image/pic_0010.jpg', _flag=cv2.IMREAD_COLOR)
    ImageShowMat(m_image)

    copy_img = m_image.copy()
    copy_img[:, :, 0] = 0
    copy_img[:, :, 1] = 0
    ImageShowMat(copy_img)
    print(type(m_image))
