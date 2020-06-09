import json, requests


class APIConsumer:
    def __init__(self):
        self.rq = requests

    def get_forecast(self, url):
        self.rq.get()
