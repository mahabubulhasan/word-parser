from pathlib import Path
from bs4 import BeautifulSoup


class Vocab:
    """Vocabulary parser for vocabulary.com"""

    def __init__(self, files):
        self.files = files
        self._words = dict()

    @staticmethod
    def _read_file(filename="list_a"):
        path = Path().absolute()
        with open(f'{path}/docs/{filename}.html', mode='r', encoding='UTF8') as f:
            return f.read()

    @staticmethod
    def _parse(html):
        soup = BeautifulSoup(html, 'html.parser')
        raw_list = soup.select('ol#wordlist > li')

        words = dict()
        for li in raw_list:
            key = li.find('a').string
            definition = li.find('div', {'class': 'definition'}).string
            words[key] = str(definition).strip()
        return words

    def words(self):
        words = dict()
        for filename in self.files:
            temp = self._parse(self._read_file(filename))
            words = {**words, **temp}

        self._words = words
        return sorted(words.keys())

    def definition(self, word):
        return self._words[word]
