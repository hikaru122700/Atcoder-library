def acsill(S, KEY):  # KEYはシフトする文字数
    num_loc = []
    # 以下に、記述してください。
    enc = ""

    for char in list(S):
        ASCII = ord(char)
        num = ASCII - 97
        num_loc.append(num)
        num = (num + KEY) % 26
        ASCII = num + 97
        enc += chr(ASCII)

    return enc  # 文字コード
    return num_loc  # 数に変換したリストを返す。
