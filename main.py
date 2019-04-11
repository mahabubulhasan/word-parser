from vocab import Vocab
from database import *
from scrapper import Scrapper
from time import time

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
def get_words(start_index):
    words = []
    for w in Words.select().order_by(Words.word).limit(10, start_index):
        words.append(w.word)

    return words


@db_session
def scrape_words(words, scrapper):
    for word in words:
        connected = scrapper.scrape(word)
        if connected:
            update_word(word, scrapper.audio(), scrapper.details())
            for line in scrapper.examples():
                save_sentence(word, line)


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
    start_time = time()
    scrapper = Scrapper()
    for index in range(0, 50, 10):
        print("scrapping started from {}".format(index))
        words = get_words(index)
        scrape_words(words, scrapper)

    scrapper.close()
    print("duration: {}".format(time() - start_time))


if __name__ == '__main__':
    main()
