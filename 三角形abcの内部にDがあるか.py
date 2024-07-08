# 点abのベクトル
def vec(a, b):
    # ベクトルを返す
    return (a[0] - b[0], a[1] - b[1])


# 三角形abcの内部に点pがあるか確認する
# 内部ならTrueを返す
def InTrianble(a, b, c, p):
    # それぞれのベクトルを計算
    ab = vec(b, a)
    bp = vec(p, b)

    bc = vec(c, b)
    cp = vec(p, c)

    ca = vec(a, c)
    ap = vec(p, a)

    # 外積(Outer Product)を求める
    OP1 = ab[0] * bp[1] - ab[1] * bp[0]
    OP2 = bc[0] * cp[1] - bc[1] * cp[0]
    OP3 = ca[0] * ap[1] - ca[1] * ap[0]

    # 外積の向き　正負がそろっていれば内側
    if (OP1 > 0 and OP2 > 0 and OP3 > 0) or (OP1 < 0 and OP2 < 0 and OP3 < 0):
        return True


'''
使い方
a, b, c, dには二次元配列のリストで渡す。
また、abcdの位置を変更して４回試す。
'''
