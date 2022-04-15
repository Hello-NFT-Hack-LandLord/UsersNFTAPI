import requests
from bs4 import BeautifulSoup
import re

class Scrapper:
    def __init__(self, user):
        self.user = user
        self.URL = "https://testnets.opensea.io"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        self.results = set()

    def user_contract(self, user_contract_address):
        url = f"/{user_contract_address}"
        return url

    def get_html(self, sub_url):
        url = self.URL + sub_url
        page = requests.get(url, headers=self.headers)
        self.soup = BeautifulSoup(page.content, "html.parser")
    
    def get_nft_links(self) -> list:
        filtered = self.soup.find_all("a", href=re.compile("^/assets/0x"), class_="styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor")
        list_urls_assets = []

        for link in filtered:
            list_urls_assets.append(link.get('href'))

        return list_urls_assets

    def get_contract_token_id(self, url):
        splited_url = url.split('/')
        #logging.info(splited_url)
        if len(splited_url) >= 4:
            contract_address = splited_url[2]
            token_id = splited_url[3]

            return (contract_address, token_id)
        return (None, None)

    def get_nft_info(self):
        for nft in self.get_nft_links():
            contract_address, token_id = self.get_contract_token_id(nft)
            
            nft_tuple = (contract_address, token_id)

            if nft_tuple != (None, None):
                self.results.add(nft_tuple)

            