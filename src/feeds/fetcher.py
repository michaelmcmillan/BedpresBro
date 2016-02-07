import requests
from config import configuration

class Fetcher:

    @classmethod
    def get(cls, url):
        response = requests.get(url, headers={
            'User-Agent': configuration['feeds']['user-agent']
        })
        return response.text
