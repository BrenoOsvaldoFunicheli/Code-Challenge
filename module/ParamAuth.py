class ParamAuth:

    def __init__(self, app_id=None, url=None, city=None):
        self.id = app_id
        self.url = url
        self.city = city

    def get_city(self):
        return self.city

    def get_url(self):
        return self.url

    def get_id(self):
        return self.id
