from bs4 import BeautifulSoup
import requests

class SoupGenerator:
    def __init__(self):
        pass

    def generate(self, url: str) -> BeautifulSoup:
        __url_data: str = self.__fetch_url_data(url)
        return self.__generate_soup(__url_data)

    def __fetch_url_data(self, url: str) -> str:
        __response = requests.get(url)
        __response.encoding = __response.apparent_encoding
        return __response.text

    def __generate_soup(self, url_data: str) -> BeautifulSoup:
        __soup = BeautifulSoup(url_data, "html.parser")
        return __soup