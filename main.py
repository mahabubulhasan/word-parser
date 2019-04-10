from vocab import Vocab
from database import *

files = ['list_a', 'list_b', 'list_c', 'list_d', 'list_e']


@db_session
def save_words():
    vocab = Vocab(files)
    words = vocab.words()

    for word in words:
        row = Words.get(word=word)

        if row:
            row.set(definition=vocab.definition(word))
        else:
            Words(word=word, definition=vocab.definition(word))


def main():
    save_words()


if __name__ == '__main__':
    main()
