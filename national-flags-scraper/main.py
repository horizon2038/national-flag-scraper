import asyncio
import json
from typing import Any
import re

from countriesscraper.soupgenerator import SoupGenerator
from countriesscraper.countriesurlscraper import CountriesURLScraper
from countriesscraper.countrynamescraper import CountryNameScraper
from countriesscraper.nationalflagscraper import NationalFlagScraper
from countriesscraper.urlabsoluteconverter import URLAbsoluteConverter
from countriesscraper.nationalflagsdownloader import NationalFlagsDownloader

class CountriesScraper:
    def __init__(self):
        self.__url: str = "https://www.mofa.go.jp/mofaj/area/index.html"
        self.__url_absolute_converter: URLAbsoluteConverter = URLAbsoluteConverter(self.__url)
        self.__soupgenerator: SoupGenerator = SoupGenerator()
        self.__countries_url_scraper: CountriesURLScraper = CountriesURLScraper(self.__soupgenerator.generate(self.__url))
        self.__national_flags_downloader: NationalFlagsDownloader = NationalFlagsDownloader("./countries/images/")

    async def main(self):
        self.__countries_url: list = self.__countries_url_scraper.find_countries_url()
        self.__countries: dict = {}
        await asyncio.gather(*(self.__fetch_countries(__country_url) for __country_url in self.__countries_url))
        self.__dumpjson(self.__countries)

    async def __fetch_countries(self, __url: str):
        try:
            __converted_url: str = self.__url_absolute_converter.convert(__url)
            __soup = self.__soupgenerator.generate(__converted_url)
            __country_name_scraper: CountryNameScraper = CountryNameScraper(__soup)
            __national_flag_scraper: NationalFlagScraper = NationalFlagScraper(__soup)
            __country_name = __country_name_scraper.find_country_name()
            __national_flag_url = self.__url_absolute_converter.convert(__national_flag_scraper.find_national_flag())
            self.__countries[__country_name] = __national_flag_url
            __country_file_name: str = "{}.gif".format(__country_name)
            self.__national_flags_downloader.download_image(__national_flag_url, __country_file_name)
            print("{}, {}".format(__country_name, __national_flag_url))
        except:
            pass

    def __dumpjson(self, countries: dict): #TODO: split json-out system and parse system
        with open("./countries/countries.json", "w+", encoding="utf-8") as file:
            json.dump(countries, file, ensure_ascii=False, indent=4)
            print("JSON OUT!")

if __name__ == "__main__":
    __countries_scraper: CountriesScraper = CountriesScraper()
    asyncio.run(__countries_scraper.main())