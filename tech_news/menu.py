import sys
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news

from termcolor import colored


def print_complete_news(news):
    for n in news:
        print(colored("URL:", "blue"), f"{n['url']}")
        print(colored("Título:", "blue"), f"{n['title']}")
        print(colored("Categoria:", "blue"), f"{n['category']}")
        print(colored("Data:", "blue"), f"{n['timestamp']}")
        print(colored("Autor:", "blue"), f"{n['writer']}")
        print(
            colored("Tempo de leitura:", "blue"),
            f"{n['reading_time']} minutos",
        )
        print(colored("Resumo:", "blue"), f"{n['summary']}\n")


def print_news(news):
    for n in news:
        print(colored("Título:", "blue"), f"{n[0]}")
        print(colored("URL:", "blue"), f"{n[1]}\n")


def exit_program():
    """
    Função que encerra o programa.
    """
    print(colored("\nEncerrando o programa.", "red"))


def print_menu():
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por categoria;")
    print(" 4 - Listar top 5 categorias;")
    print(" 5 - Sair.")


def handle_option_0():
    quantity_news = int(input("Digite quantas notícias serão buscadas: "))
    news = get_tech_news(quantity_news)
    print(
        colored(f"\n{quantity_news} notícias buscadas com sucesso!\n", "green")
    )
    print_complete_news(news)


def handle_option_1():
    title = input("Digite o título: ")
    news = search_by_title(title)
    print(colored(f"\n{len(news)} notícias encontradas!\n", "green"))
    print_news(news)


def handle_option_2():
    date_format = colored("aaaa-mm-dd: ", "yellow")
    date = input(f"Digite a data no formato {date_format}")
    news = search_by_date(date)
    print(colored(f"\n{len(news)} notícias encontradas!\n", "green"))
    print_news(news)


def handle_option_3():
    category = input("Digite a categoria: ")
    news = search_by_category(category)
    print(colored(f"\n{len(news)} notícias encontradas!\n", "green"))
    print_news(news)


def handle_option_4():
    categories = top_5_categories()
    print(colored("\nTop 5 categorias:", "green"))
    for category in categories:
        print(f"{category}")


def read_menu_option():
    while True:
        try:
            option_number = int(input("\nOpção selecionada: "))
            if option_number < 0 or option_number > 5:
                raise ValueError()
            return option_number
        except ValueError:
            print(
                colored("\nPor favor, digite um número válido.", "red"),
                file=sys.stderr,
            )


def analyzer_menu():
    menu = [
        (0, "Popular o banco com notícias", handle_option_0),
        (1, "Buscar notícias por título", handle_option_1),
        (2, "Buscar notícias por data", handle_option_2),
        (3, "Buscar notícias por categoria", handle_option_3),
        (4, "Listar top 5 categorias", handle_option_4),
        (5, "Sair", exit_program),
    ]

    while True:
        print("\nSelecione uma das opções a seguir:")
        for option in menu:
            print(f" {option[0]} - {option[1]}")
        option_number = read_menu_option()
        option = next(
            (option for option in menu if option[0] == option_number), None
        )
        option[2]()
        if option_number == 5:
            break
