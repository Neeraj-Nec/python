import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import logging

url = "https://www.flipkart.com/search?q=" 
main_url="https://www.flipkart.com/search"
product_link= "https://www.flipkart.com/apple-iphone-11-purple-128-gb/p/itmb7ca0b05522ff?pid=MOBFWQ6BEHFXGXGB&lid=LSTMOBFWQ6BEHFXGXGBBI1U9D&marketplace=FLIPKART&q=apple+11&store=tyy%2F4io&srno=s_1_11&otracker=search&fm=organic&iid=b6e5281f-a911-4e53-b6ef-7f0e57089880.MOBFWQ6BEHFXGXGB.SEARCH&ppt=None&ppn=None&ssid=g4y08abgj40000001677141013000&qH=c708fadc1c822697"
class WebScapping:
    def __init__(self,product_name, div_type):
        self.__url_type = product_name
        self.__div_type = div_type

    def get_url(self):
        global url
        flipcart_url = url + self.__url_type
        return flipcart_url

    def get_big_box(self, page):
        html_format = bs(page, 'html.parser')
        big_box = html_format.find_all("div", self.__div_type)
        return big_box

    def find_all_product(self):
        url  = str(self.get_url())
        url_client = urlopen(url)
        page = url_client.read()
        all_product = self.get_big_box(page)       # {"class":"_1AtVbE col-12-12"}
        return all_product

    def get_all_url(self):
        global main_url 
        url_list=[]
        big_box = self.find_all_product()
        for i in bog_box:
            url = main_url+(i.div.div.div.a["href"])
            url_list.append(url)
        return url_list

    def get_link_content(self):
        product_request = requests.get(product_link)
        link_content = self.get_big_box(product_request.text)
        return link_content


obj = WebScapping("apple+11", {"class":"_1AtVbE col-12-12"})
single_product_content = obj.get_link_content()
print(single_product_content)

{"class":"_1AtVbE col-12-12"}
