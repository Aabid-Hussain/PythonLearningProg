'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

res = []

for x in range(0,4):
    for y in range(0,4):
        sum_value = sum(arr[x][y:y+3]) + arr[x+1][y+1] \
                    + sum(arr[x+2][y:y+3])
        res.append(sum_value)
print(max(res))

#
# max = -100
# for i in range(4):
#     for j in range(4):
#         sum = arr[i+1][j+1]
#         for x in range(3):
#             sum += arr[i][j+x] + arr[i+2][j+x]
#         if sum > max:
#             max = sum
# print(max)