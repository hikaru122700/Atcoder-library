import random
for i in range(10):
    random_number = random.randint(0, 2)
    print(random_number)

import random

# 1から50までの数のリストを作成
numbers = list(range(1, 51))

# ランダムにシャッフル
random.shuffle(numbers)
lst =random.shuffle(numbers)
print('numbers:', lst)
# # 重複なしで50個出力
# for num in numbers:
#     print(num)


'''
あるものの中からランダムに一つ選ぶ
'''
print(sorted(numbers[:30]))
import random

# 与えられたリスト
lst = [1, 4, 7]

# 1から10までの全ての数
all_numbers = set(range(1, 11))

# lstに含まれない数のリスト
not_in_lst = list(all_numbers - set(lst))

# lstからランダムに1つ選ぶ
in_lst_random = random.choice(lst)

# not_in_lstからランダムに1つ選ぶ
not_in_lst_random = random.choice(not_in_lst)

print(f"リストに含まれるランダムな数: {in_lst_random}")
print(f"リストに含まれないランダムな数: {not_in_lst_random}")
