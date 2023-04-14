from tech_news.database import find_news_by_title


def search_by_title(title: str):
    news = find_news_by_title(title.lower())
    return [(new["title"], new["url"]) for new in news]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
