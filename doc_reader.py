from database import *
from vocab import Vocab

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


if __name__ == '__main__':
    load_words()
