import datetime


class WeekDayUtil:

    def __init__(self):
        # dict for translate
        self.rule = {
            0: "Monday"
            , 1: "Tuesday"
            , 2: "Wednesday"
            , 3: "Thursday"
            , 4: "Friday"
            , 5: "Saturday"
            , 6: "Sunday"
        }

    @staticmethod
    def remove_zero(day):
        """:returns This function format string day to get unique number instead of 0-number """
        if day[0] == '0':
            return int(day[1])
        else:
            return int(day)

    def translate(self, day):
        """:returns This function returns name of the week based dictionary"""
        return self.rule[day]

    def weekday(self, year, month, day):
        """:returns A function that returns processing of strings"""
        spc_day = datetime.datetime(int(year), self.remove_zero(month), self.remove_zero(day))
        return self.translate(spc_day.weekday())
