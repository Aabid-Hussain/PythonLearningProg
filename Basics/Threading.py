import threading

#Fuzzing
# import threading, time, random

counter = 0

def worker():

    global counter

    counter += 1
    print('The count is %d' % counter)
    print('---------------')

print('Starting Up')
for i in range(1000000000):
    threading.Thread(target=worker).start()
print("Finishing Up")

