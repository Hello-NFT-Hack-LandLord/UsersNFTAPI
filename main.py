from re import sub
from scrapper import Scrapper

def main():
    user_address = "0x1d3f85714635Df3f496A0075055078b8c4393339" #"0xc3b3928aAee37dCbDd9dD9Bf403Ec7Fe93cf9beD"
    scrapper = Scrapper(user=user_address)
    sub_url = scrapper.user_contract(user_contract_address=user_address)
    scrapper.get_html(sub_url=sub_url)

    scrapper.get_nft_info()
    print(len(scrapper.results))
    print(scrapper.results)
# 
if __name__=='__main__':
    main()