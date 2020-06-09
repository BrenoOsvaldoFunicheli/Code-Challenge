from app import Forecaster
from config import Environment
from config import Authentication


def run():

    f = Forecaster()

    lst_umbrella = f.get_umbrella_day()
    days = ", ".join(lst_umbrella)

    print("You should take an umbrella in these days: " + days)


run()
