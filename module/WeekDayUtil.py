import datetime

class WeekDayUtil:

    def __init__(self):
        # dict for translate
        self.rule = {
            0: "Segunda-Feira"
            , 1: "Terça-Feira"
            , 2: "Quarta-Feira"
            , 3: "Quinta-Feira"
            , 4: "Sexta-Feira"
            , 5: "Sabado"
            , 6: "Sabado"
        }

    def remove_zero(self, day):
        """:returns This function format string day to get unique number instead of 0-number """
        if day[0] == '0':
            return int(day[1])
        else:
            return int(day)

    def tranlate(self, day):
        """:returns This function returns name of the week based dictionary"""
        return self.rule[day]

    def weekday(self, year, month, day):
        """:returns A function that returns processing of strings"""
        spc_day = datetime.datetime(int(year), self.remove_zero(month), self.remove_zero(day))
        return self.tranlate(spc_day.weekday())