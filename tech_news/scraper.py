# Requisito 1 | Iniciando projeto
import requests
from requests import ReadTimeout
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url::text").get()
    comments_count = len(selector.css(".comment-body").getall())
    summary = "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text")
                .getall()).strip()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css("span.label::text").get()
    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    page = fetch("https://blog.betrybe.com")
    news = []
    while len(news) < amount:
        urls = scrape_novidades(page)
        for url in urls:
            content = fetch(url)
            tech_news = scrape_noticia(content)
            news.append(tech_news)
        url_next_page = scrape_next_page_link(page)
        page = fetch(url_next_page)
    noticias = news[:amount]
    create_news(noticias)
    return noticias
