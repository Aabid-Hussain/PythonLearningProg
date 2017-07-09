def is_leap(year):
    leap = False
    value_storage = int(str(int(str(year)[::-1]))[::-1])
    if value_storage % 4 == 0:
        leap = True
    else:
        if year % 100 == 0 and year % 400 == 0:
            leap = True

    return leap

while True:
    print(is_leap(int(input())))

