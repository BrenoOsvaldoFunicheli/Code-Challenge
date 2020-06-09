from module import APIConsumer, WeekDayUtil
import pandas as pd


class Forecaster:

    def __init__(self):
        self.hmd_limit = 70
        self.a = APIConsumer()  # API Consumer
        self.df_rst = self.process_forecast()  # Generate df with correct columns
        self.wdu = WeekDayUtil()    # Date Format Helper
        self.apply_trf()

    def process_forecast(self):
        # Process certain API query
        self.a.process_result()

        f = self.a.get_forecast()
        ds = []

        # Iteration over all dictionaries
        # to prepare important columns
        for i in f:
            i['main']['dt_txt'] = i['dt_txt']
            ds.append(i['main'])
        return pd.DataFrame(ds)

    def apply_trf(self):
        """
        :returns This procedure returns correct name of the week based calc of the date
        """
        self.df_rst['dt_txt'] = self.df_rst['dt_txt'].apply(
            lambda x: self.wdu.weekday(str(x)[0:4], str(x)[5:7], str(x)[8:10]))


if __name__ == '__main__':

    # df = Forecaster().df_rst
    # df.dt_txt = df.dt_txt.apply(lambda x: str(x)[8:10])
    a = Forecaster()
    print(a.df_rst)

