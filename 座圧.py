def zaatsu(before_list):
    set_sort = sorted(list(set(before_list))) # 重複排除とソート
    rank = {x:i+1 for i,x in enumerate(set_sort)} # 各値に順位づけ
    after_list = []
    for tmp in before_list:
        after_list.append(rank[tmp])
    return after_list

A = list(map(int, input().split()))
print(zaatsu(A))

'''
以下は重複排除なしver
'''
def zaatsu(before_list):
    set_sort = sorted(before_list) # 重複排除とソート
    rank = {x:i+1 for i,x in enumerate(set_sort)} # 各値に順位づけ
    after_list = []
    for tmp in before_list:
        after_list.append(rank[tmp])
    return after_list
