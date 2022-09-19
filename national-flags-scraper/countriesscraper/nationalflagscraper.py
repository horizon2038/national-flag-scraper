from typing import Any
from bs4 import BeautifulSoup
import requests

class NationalFlagScraper:
    def __init__(self, beautifulsoup: BeautifulSoup):
        self.soup: BeautifulSoup = beautifulsoup

    def find_national_flag(self) -> str:
        return self.__find_data_bytag()

    def __find_data_bytag(self) -> str:
        __parameter: str = "div#contents-header > h2 > span > img[src]"
        __fetched_data: Any = self.soup.select(__parameter)[0].get("src")
        return __fetched_data