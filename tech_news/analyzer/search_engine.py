from tech_news.database import (
    find_news_by_title,
    find_news_by_date,
    find_news_by_category,
)
from datetime import datetime


def search_by_title(title: str) -> list[tuple]:
    news = find_news_by_title(title)
    return [(new["title"], new["url"]) for new in news]


def search_by_date(date: str) -> list[tuple]:
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = datetime.strftime(date_obj, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Data inválida")

    news = find_news_by_date(formatted_date.replace("-", "/"))
    return [(new["title"], new["url"]) for new in news]


def search_by_category(category: str) -> list[tuple]:
    news = find_news_by_category(category)
    return [(new["title"], new["url"]) for new in news]
