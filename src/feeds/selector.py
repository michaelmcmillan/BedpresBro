from bs4 import BeautifulSoup

class Selector:

    @classmethod
    def find(cls, html, selector):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.select(selector)

