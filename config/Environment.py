class Environment:

    def __init__(self):
        self.app_id = "439d4b804bc8187953eb36d2a8c26a02"
        self.url = "https://samples.openweathermap.org/data/2.5/forecast"
        self.city_id = "6322515"

    def _get_api_key(self):
        """
        Function returns appid need in the url search
        :arg
        """
        return self.app_id

    def _get_base_url(self):
        return self.url

    def _get_city(self):
        """
        :returns This method returns city_id for certain city

        """
        return self.city_id

    def make_search_url(self):
        """
        :returns A complete url for test in the
        """
        return self._get_base_url() + "?id=" + self._get_city() + "&appid=" + self._get_api_key()


if __name__ == '__main__':
    e = Environment()
    url = e.make_search_url()
    print(url)
