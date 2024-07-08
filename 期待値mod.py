MOD = 998244353


def mod_inv(x, mod):
    return pow(x, mod - 2, mod)


def expected_value_mod(numerator, denominator, mod):
    # 分母の逆元を求める
    inv_denominator = mod_inv(denominator, mod)

    # 期待値を計算する
    result = (numerator * inv_denominator) % mod

    return result


# # 使用例
# numerator = 3
# denominator = 2
#
# result = expected_value_mod(numerator, denominator, MOD)
