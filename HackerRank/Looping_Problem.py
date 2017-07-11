n = int(input("Enter number to be tabled: ").strip())

for get_input_iter in range(1, 11):
    print("{} x {} = {}".format(n, get_input_iter, n * get_input_iter))