import requests
from typing import Any

class NationalFlagsDownloader:
    def __init__(self, location: str) -> None:
        self.location = location

    def download_image(self, url: str, filename: str):
        __url_data: Any = requests.get(url).content
        self.__save_image(__url_data, filename)

    def __save_image(self, url_data: Any, filename: str):
        filepath: str = "{}{}".format(self.location, filename)
        with open(filepath, mode='wb') as file:
            file.write(url_data)

if __name__ == "__main__":
    national_flags_downloader: NationalFlagsDownloader = NationalFlagsDownloader("./countries/images/")
    national_flags_downloader.download_image("https://m.media-amazon.com/images/I/51jKntGbt6L._AC_SY355_.jpg", "while1lt2.jpg")