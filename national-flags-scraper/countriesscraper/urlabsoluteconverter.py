from urllib import parse

class URLAbsoluteConverter:
    def __init__(self, url: str):
        self.base_url: str = url

    def convert(self, relative_url: str):
        return parse.urljoin(self.base_url, relative_url)
    
