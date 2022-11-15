from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_title = search_news({"title": {"$regex": title, "$options": "i"}})

    result = [(news["title"], news["url"]) for news in news_title]

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        iso_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news_date = search_news({"timestamp": iso_format})
        result = [(news["title"], news["url"]) for news in news_date]
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    tags = {"tags": {"$regex": tag, "$options": "i"}}
    news_tag = search_news(tags)
    result = [(news['title'], news['url']) for news in news_tag]
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    categorie = {"category": {"$regex": category, "$options": "i"}}
    news_category = search_news(categorie)
    result = [(news['title'], news['url']) for news in news_category]
    return result
