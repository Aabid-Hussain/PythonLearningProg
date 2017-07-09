n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
count1 = 0
count2 = 0
count3 = 0

for a_t in arr:
    if a_t > 0:
        count1 += 1
    elif a_t < 0:
        count2 += 1
    else:
        count3 += 1

print("{:8.6f}\n{:8.6f}\n{:8.6f}".format(
    count1 / len(arr), count2 / len(arr), count3 / len(arr)))
