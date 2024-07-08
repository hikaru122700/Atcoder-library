import time

start_time = time.time()
a = 0
# 測りたい処理をここに書く
for i in range(10**8):
    a += 1
end_time = time.time()
execution_time = time.time() - start_time
print("処理時間:", execution_time, "秒")
