import requests
from time import sleep
from bs4 import BeautifulSoup

HEADERS = {"user-agent": "Fake user-agent"}


def fetch(url: str) -> str | None:
    try:
        page = requests.get(url, headers=HEADERS, timeout=3)
    except requests.ReadTimeout:
        return None

    sleep(1)
    return page.text if page.status_code == 200 else None


def scrape_updates(html_content: str) -> list[str] | None:
    soup = BeautifulSoup(html_content, "html.parser")
    updates = soup.find_all("a", {"class": "cs-overlay-link"})

    return (
        [update["href"] for update in updates]
        if isinstance(updates, list)
        else None
    )


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
