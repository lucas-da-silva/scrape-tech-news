from tech_news.database import find_news_by_title, find_news_by_date
from datetime import datetime


def search_by_title(title: str) -> list[tuple[str, str]]:
    news = find_news_by_title(title.lower())
    return [(new["title"], new["url"]) for new in news]


def search_by_date(date: str):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = datetime.strftime(date_obj, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Data inválida")

    news = find_news_by_date(formatted_date.replace("-", "/"))
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
