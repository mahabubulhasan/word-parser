from pathlib import Path

from bs4 import BeautifulSoup


def _read_file(filename="list_a"):
    path = Path().absolute()
    with open(f'{path}/docs/{filename}.html', mode='r', encoding='UTF8') as f:
        return f.read()


def _parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    raw_list = soup.select('ol#wordlist > li')

    words = dict()

    for li in raw_list:
        key = li.find('a').string
        definition = li.find('div', {'class': 'definition'}).string
        words[key] = str(definition).strip()

    return words


def word_list(files):
    words = dict()
    for filename in files:
        temp = _parse(_read_file(filename))
        words = {**words, **temp}

    return words
