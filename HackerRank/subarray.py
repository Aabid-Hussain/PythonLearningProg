def maxLength(s, k):
    lengths = [0 for x in range(k)]
    for i in range(1,k+1):
        for j in range(len(s)):
            if s[j] <= i and lengths[i - s[j]] + 1 > lengths[i]:
                lengths[i] = lengths[i - s[j]] + 1
        if i + 1 == len(s):
            break
    return lengths[-1]


arr = [1,2,3]
Sum = 0


# for i in range(len(arr)):
#     for j in range(len(arr)-1, i-1, -1):
#         Sum += arr[j]
#

print(Sum)
for i in range(len(arr)):
    j = i+1
    if j<len(arr):
        Sum += arr[i] + arr[j]

print(Sum)

arr = list((75, 180))

ap = str(arr).lstrip('([').rstrip(')]').split(',')


print(ap)

























