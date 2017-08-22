import pickle


lines = open("E:\ME\cities_and_times.txt").readlines()

lines.sort()

cities = []

for line in lines:
    *c, day, time = line.split()
    hours, minutes = time.split(":")
    cities.append((" ".join(c), day,
                   (int(hours), int(minutes))))

fh = open("E:\ME\cities_and_times.pkl",'wb')
pickle.dump(cities, fh)
