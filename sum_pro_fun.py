from timeit import Timer

commands = ["%s(%s);", "len(d);d=%s(%s)", "for i in d:\n\tpass;d=%s(%s)"]
functions = ["range", "xrange"]
params = range(10000, 100001, 10000)

for command in commands:
    for function in functions:
        print command % (function, 'x')
        for param in params:
            torun = str(command % (function, str(param)))
            torun, setup = torun.split(';')
            print str(param) + '\t' + str(Timer(torun, setup).timeit(1000))