mocked_find_news = [
    {
        "url": "https://blog.betrybe.com/tecnologia/cabos-de-rede/",
        "title": "Cabos de rede: o que são, quais os tipos e como crimpar?",
        "timestamp": "10/04/2023",
        "writer": "Dayane Arena dos Santos",
        "reading_time": 9,
        "summary": "Os cabos de rede são itens extremamente necessários",
        "category": "Tecnologia",
    },
    {
        "url": (
            "https://blog.betrybe.com/desenvolvimento-web/"
            "estruturas-de-repeticao/"
        ),
        "title": (
            "Estruturas de repetição: quais as 4 principais e quando usá-las?"
        ),
        "timestamp": "05/04/2023",
        "writer": "Vinicius Martins",
        "reading_time": 5,
        "summary": "As estruturas de repetição estão muito presentes na vida ",
        "category": "Desenvolvimento Web",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/website-development/",
        "title": (
            "Website development: o que é, o que faz e salário! "
            "O guia inicial!"
        ),
        "timestamp": "31/03/2023",
        "writer": "Lucas Custódio",
        "reading_time": 13,
        "summary": "O Website development pode ser encontrado no mercado de",
        "category": "Tecnologia",
    },
]

mocked_news_for_available_time = {
    "readable": [
        {
            "chosen_news": [
                (
                    "Cabos de rede: o que são, quais os tipos e "
                    "como crimpar?",
                    9,
                )
            ],
            "unfilled_time": 1,
        },
        {
            "chosen_news": [
                (
                    "Estruturas de repetição: quais as 4 "
                    "principais e quando usá-las?",
                    5,
                )
            ],
            "unfilled_time": 5,
        },
    ],
    "unreadable": [
        (
            "Website development: o que é, o que faz e salário! O guia "
            "inicial!",
            13,
        )
    ],
}
