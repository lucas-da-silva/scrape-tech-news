import sys
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news


def tech_news():
    quantity_news = int(input("Digite quantas notícias serão buscadas:"))
    get_tech_news(quantity_news)


def title():
    title = input("Digite o título:")
    search_by_title(title)


def date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    search_by_date(date)


def category():
    category = input("Digite a categoria:")
    search_by_category(category)


def exit():
    print("Encerrando script")


def analyzer_menu():
    menu_options = {
        0: tech_news,
        1: title,
        2: date,
        3: category,
        4: top_5_categories,
        5: exit,
    }

    try:
        option = int(
            input(
                (
                    "Selecione uma das opções a seguir:\n"
                    " 0 - Popular o banco com notícias;\n"
                    " 1 - Buscar notícias por título;\n"
                    " 2 - Buscar notícias por data;\n"
                    " 3 - Buscar notícias por categoria;\n"
                    " 4 - Listar top 5 categorias;\n"
                    " 5 - Sair.\n"
                )
            )
        )
        menu_options[option]()
    except (ValueError, KeyError):
        print("Opção inválida", file=sys.stderr)
