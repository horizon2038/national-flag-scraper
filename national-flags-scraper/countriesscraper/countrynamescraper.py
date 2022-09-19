from typing import Any
from bs4 import BeautifulSoup
import re

class CountryNameScraper:
    def __init__(self, beautifulsoup: BeautifulSoup):
        self.soup: BeautifulSoup = beautifulsoup
        self.__pattern_japanese: str = "^[^a-zA-Z]+"
        self.__pattern_english: str = "[A-Z][A-Za-z ]+"

    def find_country_name(self) -> str:
        __data_by_tag: str = self.__find_data_bytag()
        __shaped_country_name = self.__shaping_country_name(__data_by_tag)
        return __shaped_country_name

    def __find_data_bytag(self) -> str:
        __parameter: str = "div#contents-header > h2 > span"
        __fetched_data: str = self.soup.select(__parameter)[1].text
        return __fetched_data

    def __shaping_country_name(self, country_name: str) -> str: #TODO: split json and parse script
        __country_name_japanese: str = re.search(self.__pattern_japanese, country_name).group()
        __country_name_english: str = re.search(self.__pattern_english, country_name).group()
        return "{}_{}".format(__country_name_japanese, __country_name_english)