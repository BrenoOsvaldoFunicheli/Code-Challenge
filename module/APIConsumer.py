import requests
from config import Environment


class APIConsumer:
    def __init__(self):
        """
            ---- Attributes----
            self.rq : abstraction of the methods present in request
            self.env:
        """
        self.rq = requests
        self.env = Environment()
        self.url = self.env.make_search_url()
        self.result = ''

    def is_valid(self, status):
        if status == 200:
            return True

    def _get_data(self):
        sts = self.rq.get(self.url)

        # verification of the status on response query
        if self.is_valid(sts.status_code):
            return sts.json()

    def process_result(self):
        # parcial result of the query on the API
        prc_result = self._get_data()
        self.result = prc_result['list']

    def get_forecast(self):
        return self.result


if __name__ == '__main__':
    a = APIConsumer()
    a.process_result()
    rs = a.get_forecast()
    print(rs)
