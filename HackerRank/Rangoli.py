import string

string_value_ascii = string.ascii_lowercase  # your code goes here
empty_list = []
size = int(input())
for ran_value in range(size):
    temp_str = "-".join(string_value_ascii[ran_value:size])
    empty_list.append(temp_str[::-1] + temp_str[1:])

width_len = len(empty_list[0])

# print upper half of the rangoli
for ran_value in range(size - 1, 0, -1):
    print(empty_list[ran_value].center(width_len, "-"))

# print next half of the rangoli
for ran_value in range(size):
    print(empty_list[ran_value].center(width_len, "-"))
