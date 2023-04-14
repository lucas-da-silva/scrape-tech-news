import requests
from time import sleep
from bs4 import BeautifulSoup
from tech_news.database import create_news


HEADERS = {"user-agent": "Fake user-agent"}
BLOG_TRYBE_URL = "https://blog.betrybe.com"


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


def scrape_next_page_link(html_content: str) -> str | None:
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", {"class": "next"})
    return next_page["href"] if next_page else None


def scrape_url(soup: BeautifulSoup) -> str | None:
    url = soup.find("link", {"rel": "canonical"})
    return url["href"] if url else None


def scrape_title(soup: BeautifulSoup) -> str | None:
    title = soup.find("h1", {"class": "entry-title"})
    return title.text.rstrip() if title else None


def scrape_timestamp(soup: BeautifulSoup) -> str | None:
    timestamp = soup.find("li", {"class": "meta-date"})
    return timestamp.text if timestamp else None


def scrape_writer(soup: BeautifulSoup) -> str | None:
    writer = soup.find("span", {"class": "author"})
    return writer.a.text if writer else None


def scrape_reading_time(soup: BeautifulSoup) -> int | None:
    reading_time = soup.find("li", {"class": "meta-reading-time"})
    if not reading_time:
        return None

    reading_time_number = "".join(filter(str.isdigit, reading_time.text))
    return int(reading_time_number)


def scrape_summary(soup: BeautifulSoup) -> str | None:
    summary = soup.find("div", {"class": "entry-content"})
    return summary.p.text.rstrip() if summary else None


def scrape_category(soup: BeautifulSoup) -> str | None:
    category = soup.find("div", {"class": "meta-category"}).a.find(
        "span", {"class": "label"}
    )
    return category.text if category else None


def scrape_news(html_content: str) -> dict[str, str | int | None]:
    soup = BeautifulSoup(html_content, "html.parser")

    return {
        "url": scrape_url(soup),
        "title": scrape_title(soup),
        "timestamp": scrape_timestamp(soup),
        "writer": scrape_writer(soup),
        "reading_time": scrape_reading_time(soup),
        "summary": scrape_summary(soup),
        "category": scrape_category(soup),
    }


def get_tech_news(amount: int):
    page_url = BLOG_TRYBE_URL
    posts = []
    while len(posts) < amount:
        page = fetch(page_url)
        post_links = scrape_updates(page)
        for link in post_links:
            if len(posts) >= amount:
                break
            post = scrape_news(fetch(link))
            posts.append(post)
        page_url = scrape_next_page_link(page)

    create_news(posts)
    return posts
