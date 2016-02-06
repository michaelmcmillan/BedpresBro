import requests
from bs4 import BeautifulSoup
from config import configuration

class Feed:

    def download(self, url):
        response = requests.get(url, headers={
            'User-Agent': configuration['feeds']['user-agent']
        })
        return response.text

    def selector(self, html, selector):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.select(selector)

    def get_events(self):
        pass
