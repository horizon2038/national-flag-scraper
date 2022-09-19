import re

__pattern_japanese: str = "^[^a-zA-Z]+"
__pattern_english: str = "[A-Z][A-Za-z ]+"
def __shaping_country_name(country_name: str) -> str: #TODO: split json and parse script
        __country_name_japanese: str = re.search(__pattern_japanese, country_name).group()
        __country_name_english: str = re.search(__pattern_english, country_name).group()
        return "{}/{}".format(__country_name_japanese, __country_name_english)

if __name__ == "__main__":
    source = "アイスランド共和国Republic of Iceland"
    print(__shaping_country_name(source))