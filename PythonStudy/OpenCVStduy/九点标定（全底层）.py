f"""
这是自己在网上找的仿射变换的求解，打算用来做九点标定
"""


def affine_fit(from_pts, to_pts):
    q = from_pts
    p = to_pts
    if len(q) != len(p) or len(q) < 1:
        print("原始点和目标点的个数必须相同.")
        return False

    dim = len(q[0])  # 维度
    if len(q) < dim:
        print("至少为9个点.")
        return False

    # 新建一个空的 维度 x (维度+1) 矩阵 并填满
    c = [[0.0 for _a in range(dim)] for _i in range(dim + 1)]
    for j in range(dim):
        for k in range(dim + 1):
            for i in range(len(q)):
                qt = list(q[i]) + [1]
                c[k][j] += qt[k] * p[i][j]

    # 新建一个空的 (维度+1) x (维度+1) 矩阵 并填满
    _q = [[0.0 for _a in range(dim)] + [0] for _i in range(dim + 1)]
    for qi in q:
        qt = list(qi) + [1]
        for i in range(dim + 1):
            for j in range(dim + 1):
                _q[i][j] += qt[i] * qt[j]

    # 判断原始点和目标点是否共线，共线则无解. 耗时计算，如果追求效率可以不用。
    # 其实就是解n个三元一次方程组
    def gauss_jordan(m, eps=1.0 / (10 ** 10)):
        (h, w) = (len(m), len(m[0]))
        for y in range(0, h):
            max_row = y
            for y2 in range(y + 1, h):
                if abs(m[y2][y]) > abs(m[max_row][y]):
                    max_row = y2
            (m[y], m[max_row]) = (m[max_row], m[y])
            if abs(m[y][y]) <= eps:
                return False
            for y2 in range(y + 1, h):
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
        for y in range(h - 1, 0 - 1, -1):
            c = m[y][y]
            for y2 in range(0, y):
                for x in range(w - 1, y - 1, -1):
                    m[y2][x] -= m[y][x] * m[y2][y] / c
            m[y][y] /= c
            for x in range(h, w):
                m[y][x] /= c
        return True

    _m = [_q[i] + c[i] for i in range(dim + 1)]
    if not gauss_jordan(_m):
        print("错误，原始点和目标点也许是共线的.")

        return False

    class Transformation:
        """对象化仿射变换."""

        @staticmethod
        def ToString():
            res = ""
            for j in range(dim):
                _str = "x%d' = " % j
                for i in range(dim):
                    _str += "x%d * %f + " % (i, _m[i][j + dim + 1])
                _str += "%f" % _m[dim][j + dim + 1]
                res += _str + "\n"
            return res

        @staticmethod
        def Transform(pt):
            res = [0.0 for a in range(dim)]
            for j in range(dim):
                for i in range(dim):
                    res[j] += pt[i] * _m[i][j + dim + 1]
                res[j] += _m[dim][j + dim + 1]
            return res

    return Transformation()


def test():
    from_pt = [[3372.582, 609.573],
               [3570.364, 1520.764],
               [3709.595, 2427.982],
               [1791.536, 594.729],
               [2037.180, 1475.478],
               [2224.129, 2361.770],
               [224.911, 716.184],
               [512.556, 1571.338],
               [745.420, 2431.021]]  # 输入点坐标对

    to_pt = [[-107, 218],
             [-117, 218],
             [-127, 218],
             [-107, 228],
             [-117, 228],
             [-127, 228],
             [-107, 238],
             [-117, 238],
             [-127, 238]]  # 输出点坐标对

    trn = affine_fit(from_pt, to_pt)

    if trn:
        print("转换公式:")
        print(trn.ToString())

        err = 0.0
        for i in range(len(from_pt)):
            fp = from_pt[i]
            tp = to_pt[i]
            t = trn.Transform(fp)
            print("%s => %s ~= %s" % (fp, tuple(t), tp))
            err += ((tp[0] - t[0]) ** 2 + (tp[1] - t[1]) ** 2)

        print(f"拟合误差 = {(err / 9) ** 0.5}")


if __name__ == "__main__":
    print("测试最小二乘法求解九点标定的六参数仿射变换矩阵：")
    test()
