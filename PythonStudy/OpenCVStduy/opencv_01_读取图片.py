import cv2


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


def ImageShow(_img, _name="temp", _info=""):
    """
    封装opencv显示图像 https://www.wolai.com/zeros/t7b5k4dF1d7zdBpN3XhhJz?theme=light
    @param _img:
    @param _name:
    @param _info:
    @return:
    """
    if _info:
        print(_info)

    cv2.namedWindow(_name, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(_name, _img)

    key = cv2.waitKey(0)
    if key == 27:  # 按ESC退出
        cv2.destroyAllWindows()
    elif key == ord('s'):  # 按S保存在当前文件夹下
        cv2.imwrite(_name + '.jpg', _img)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    image = ImageRead(r"pic_0015.jpg", cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ImageShow(image, 'picgary')
