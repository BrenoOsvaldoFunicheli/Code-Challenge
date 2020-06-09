from config.settings import Environment


class Authentication:

    def __init__(self, param_obj=None, make_auto=True):
        self.e = Environment()
        if make_auto:
            self.make_environment()
        else:
            self.app_id = param_obj.get_id()
            self.url = param_obj.get_url()
            self.city_id = param_obj.get_city()

    def _get_api_key(self):
        """
        :returns Function returns appid need in the url search
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

    def make_environment(self, param_auth=None, method='auto'):
        """
            :returns This method populate the configure of the url
        """
        if method == 'auto':
            self.app_id = self.e.get_app_key()
            self.url = self.e.get_base_url()
            self.city_id = self.e.get_city_id()

        else:
            self.app_id = param_auth.get_id()
            self.url = param_auth.get_url()
            self.city_id = param_auth.get_city()


if __name__ == '__main__':
    e = Authentication()
    url = e.make_search_url()
    print(url)
