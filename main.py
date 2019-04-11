from vocab import Vocab
from database import *
from scrapper import Scrapper

files = ['list_a', 'list_b', 'list_c', 'list_d', 'list_e']


@db_session
def load_words():
    """loads words from html files to sqlite database, should be called only once"""

    vocab = Vocab(files)
    words = vocab.words()

    for word in words:
        row = Words.get(word=word)
        if row:
            row.set(definition=vocab.definition(word))
        else:
            Words(word=word, definition=vocab.definition(word))


@db_session
def get_words():
    words = []
    for w in Words.select().order_by(Words.word).limit(5):
        words.append(w.word)

    return words


@db_session
def scrape_words(words):
    print("Scrapping started....")
    scrapper = Scrapper()
    for word in words:
        scrape = scrapper.scrape(word)
        update_word(word, scrape.audio(), scrape.details())
        for line in scrape.examples():
            save_sentence(word, line)

    scrapper.close()


def update_word(word, audio, details):
    """should be called from inside function with db_session"""
    row = Words.get(word=word)
    if row:
        row.set(audio=audio, details=details)


def save_sentence(word, sentence):
    row = Examples.select(lambda c: c.word == word and c.sentence == sentence).exists()
    if not row:
        Examples(word=word, sentence=sentence)


def main():
    # load_words()
    words = get_words()
    scrape_words(words)


if __name__ == '__main__':
    main()
