from typing import Any
from bs4 import BeautifulSoup

class CountriesURLScraper:
    def __init__(self, beautifulsoup: BeautifulSoup):
        self.soup: BeautifulSoup = beautifulsoup

    def find_countries_url(self) -> list:
        __data_by_tag: list = self.__find_data_bytag()
        __countries_url: list = list(map(lambda x: x.get("href"), __data_by_tag))
        return __countries_url

    def __find_data_bytag(self) -> list:
        __parameter: str = "li.styled2 > a[href]"
        __fetched_data: Any = self.soup.select(__parameter)
        return __fetched_data