# Requisito 1 | Iniciando projeto
import requests
from requests import ReadTimeout
import time
from parsel import Selector


def fetch(url):
    """Seu código deve vir aqui"""
    fakeHeaders = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=3, headers=fakeHeaders)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    urls = selector.css(".entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url_next_page = selector.css(".next ::attr(href)").get()
    return url_next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
