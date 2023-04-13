import requests
from time import sleep

HEADERS = {"user-agent": "Fake user-agent"}


def fetch(url: str) -> str | None:
    try: 
        page = requests.get(url, headers=HEADERS, timeout=3)
    except requests.ReadTimeout:
        return None
    
    sleep(1)
    return page.text if page.status_code == 200 else None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
