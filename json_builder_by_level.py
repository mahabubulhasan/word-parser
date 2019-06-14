import json
from database import *


@db_session
def get_words():
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    e_list = []
    f_list = []
    g_list = []
    h_list = []
    i_list = []
    j_list = []
    k_list = []
    l_list = []
    m_list = []
    n_list = []
    o_list = []
    p_list = []
    q_list = []
    r_list = []
    s_list = []
    t_list = []
    u_list = []
    v_list = []
    w_list = []
    x_list = []
    y_list = []
    z_list = []

    for w in Words.select().order_by(Words.word):
        add_group(w, 'a', a_list)
        add_group(w, 'b', b_list)
        add_group(w, 'c', c_list)
        add_group(w, 'd', d_list)
        add_group(w, 'e', e_list)
        add_group(w, 'f', f_list)
        add_group(w, 'g', g_list)
        add_group(w, 'h', h_list)
        add_group(w, 'i', i_list)
        add_group(w, 'j', j_list)
        add_group(w, 'k', k_list)
        add_group(w, 'l', l_list)
        add_group(w, 'm', m_list)
        add_group(w, 'n', n_list)
        add_group(w, 'o', o_list)
        add_group(w, 'p', p_list)
        add_group(w, 'q', q_list)
        add_group(w, 'r', r_list)
        add_group(w, 's', s_list)
        add_group(w, 't', t_list)
        add_group(w, 'u', u_list)
        add_group(w, 'v', v_list)
        add_group(w, 'w', w_list)
        add_group(w, 'x', x_list)
        add_group(w, 'y', y_list)
        add_group(w, 'z', z_list)

    word_list = []
    for i in range(1, 190):
        list_append(word_list, a_list)
        list_append(word_list, b_list)
        list_append(word_list, c_list)
        list_append(word_list, d_list)
        list_append(word_list, e_list)
        list_append(word_list, f_list)
        list_append(word_list, g_list)
        list_append(word_list, h_list)
        list_append(word_list, i_list)
        list_append(word_list, j_list)
        list_append(word_list, k_list)
        list_append(word_list, l_list)
        list_append(word_list, m_list)
        list_append(word_list, n_list)
        list_append(word_list, o_list)
        list_append(word_list, p_list)
        list_append(word_list, q_list)
        list_append(word_list, r_list)
        list_append(word_list, s_list)
        list_append(word_list, t_list)
        list_append(word_list, u_list)
        list_append(word_list, v_list)
        list_append(word_list, w_list)
        list_append(word_list, y_list)
        list_append(word_list, z_list)

    return word_list


def list_append(word_list, lst):
    if lst:
        word_list.append(lst.pop(0))


def definition(w):
    return {
        'word': w.word,
        'definition': w.definition,
        'details': w.details,
        'examples': get_examples(w.word)
    }


def add_group(w, cond, lst):
    if str.startswith(w.word, cond):
        lst.append(definition(w))


def get_examples(word):
    examples = []
    for e in Examples.select(lambda c: c.word == word):
        examples.append(e.sentence)

    return examples


def write_file(content):
    with open("data/words_random.json", 'w+') as f:
        f.write(content)
        print('file write successful!')


if __name__ == '__main__':
    words = get_words()
    write_file(json.dumps(words))
