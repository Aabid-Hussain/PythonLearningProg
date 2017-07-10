n = 5
arr = map(int, input().split())

temp_list = list(arr)
 #temp_list.sort()

#
# temp_list = list(set(temp_list))
# temp_list.sort()
# m = n - len(temp_list)
# print(temp_list[n - m - 2])

temp = sorted(list(set(sorted(temp_list))))

m = len(temp_list) - len(temp)


print(temp[n - m - 2])