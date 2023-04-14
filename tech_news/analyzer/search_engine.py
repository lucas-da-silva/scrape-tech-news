from tech_news.database import db
from datetime import datetime
import re


def search_by_title(title: str) -> list[tuple]:
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


def search_by_date(date: str) -> list[tuple]:
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = datetime.strftime(date_obj, "%d-%m-%Y").replace(
            "-", "/"
        )
    except ValueError:
        raise ValueError("Data inválida")

    news = db.news.find({"timestamp": {"$regex": formatted_date}})
    return [(new["title"], new["url"]) for new in news]


def search_by_category(category: str) -> list[tuple]:
    regex_category = re.escape(category)
    news = db.news.find(
        {"category": {"$regex": regex_category, "$options": "i"}}
    )
    return [(new["title"], new["url"]) for new in news]
