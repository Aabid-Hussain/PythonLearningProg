def pair(a,k):

    sorted(a)
    answer = 0

    for i in range(0,len(a)):
        for j in range(1,len(a)):
            if a[j]-a[i] == k:
                answer += 1

    return answer

a = [1,5,3,2,4]
k = 2

print(pair(a,k))
