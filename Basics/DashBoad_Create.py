def begin():
    dem = input('enter a number for a square demensioned game board: ')

    try:
        if int(dem) < 1:
            print("Must be a number")
            begin()
        else:
            pass
    except ValueError:
        print('Must be a positive number')
        begin()

    line1 = []
    line2 = []

    for a in range(int(dem)):
        line1.append(' --- ')

    for b in range(int(dem)):
        line2.append('|    ')

        if b == (int(dem) - 1):
            line2.append('|')

    line3 = (''.join(line1))

    line4 = (''.join(line2))

    for c in range(int(dem)):
        print(line3)
        print(line4)
        if c == (int(dem) - 1):
            print(line3)
    #begin()

begin()