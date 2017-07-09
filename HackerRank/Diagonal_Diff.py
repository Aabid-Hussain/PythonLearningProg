
n = 3#int(input().strip())
a = [[11,2,4],[4,5,6],[10,8,-12]]
Sum_first = 0
Sum_Sec = 0
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             Sum_first += a[i][j]

row, col = 0,n-1
while row < n and col >= 0:
    Sum_Sec += a[row][col]
    row += 1
    col -= 1

i , j = 0,0

while i<n and j<n:
    Sum_first += a[i][j]
    i += 1
    j += 1

print(abs(Sum_first - Sum_Sec))