from pathlib import Path

from bs4 import BeautifulSoup

files = ['list_a', 'list_b', 'list_c', 'list_d', 'list_e']


def read_file(filename="list_a"):
    path = Path().absolute()
    with open(f'{path}/docs/{filename}.html', mode='r', encoding='UTF8') as f:
        return f.read()


def parse_word_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    raw_list = soup.select('ol#wordlist > li')

    word_list = []

    for li in raw_list:
        entry = {
            'word': li.find('a').string,
            'definition': li.find('div', {'class': 'definition'}).string
        }

        word_list.append(entry)

    return word_list


def main():
    for file in files:
        text = read_file(file)
        print(parse_word_list(text))
        print('-------------')


if __name__ == '__main__':
    main()
