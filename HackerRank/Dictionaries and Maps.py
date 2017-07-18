'''
n =  int(input())
dict_store_key = list(input().strip().split("\n") for _ in range(n))
dict_store = {}

# for i in range(len(dict_store_key)-1):
#     a.append(str(dict_store_key[i]).lstrip("['").rstrip("']").split(" "))

# print(a.items())
# print(dict_store_key)

for i in dict_store_key:
    a = str(i).lstrip("['").rstrip("']").split(" ")
    dict_store[a[0]] = a[1]

for _ in range(n):

    dict_store_value = input().strip()
    if dict_store_value in dict_store.keys():
        print("{}={}".format(dict_store_value, dict_store[dict_store_value]))
    else:
        print("Not found")
'''
N = int(input())
phonebook = {}

for i in range(N):
    key, value = input().split()
    phonebook[key] = int(value)

for i in range(N):
    query = input()
    #if phonebook.get(query, "Not found") == "Not found":
    if not phonebook.get(query):
        print("Not found")
    else:
        print(query, '=', phonebook.get(query), sep='')