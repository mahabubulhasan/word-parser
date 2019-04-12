import json
from database import *


@db_session
def get_words():
    word_list = []
    for w in Words.select().order_by(Words.word):
        word_list.append({
            'word': w.word,
            'definition': w.definition,
            'details': w.details,
            'examples': get_examples(w.word)
        })

    return word_list


def get_examples(word):
    examples = []
    for e in Examples.select(lambda c: c.word == word):
        examples.append(e.sentence)

    return examples


def write_file(content):
    with open("data/words.json", 'w+') as f:
        f.write(content)
        print('file write successful!')


if __name__ == '__main__':
    words = get_words()
    write_file(json.dumps(words))
