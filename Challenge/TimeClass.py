# {}:{:02d}:{:02d}

class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hrs):
        self.__hour = hrs

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, mins):
        self.__minute = mins

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, sec):
        self.__second = sec

    def __str__(self):

        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, otherTime):
        new_time = Time()
        # Add the seconds and correct if sum >= 60
        if (self.second + otherTime.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + otherTime.second) - 60

        else:
            new_time.second = self.second + otherTime.second

        # Add the minutes and correct if sum >= 60
        if (self.minute + otherTime.minute) > 60:
            self.hour += 1
            new_time.minute = (self.minute + otherTime.minute) - 60
        else:
            new_time.minute = (self.minute + otherTime.minute)

        # Add the hours and correct if sum > 24

        if (self.hour + otherTime.hour) > 24:
            new_time.hour = (self.hour + otherTime.hour) - 24
        else:
            new_time.hour = (self.hour + otherTime.hour)

        return new_time

    def __sub__(self, secondTime):
       subValue = Time()

       if (self.second > secondTime.second)

       return subValue






def main():
    time1 = Time(1, 20, 30)

    print time1

    time2 = Time(2, 41, 30)

    print time2

    print time1 + time2
    print

    print time1 - time2


main()
