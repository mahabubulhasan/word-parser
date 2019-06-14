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

    word_list = {
        'a': len(a_list),
        'b': len(b_list),
        'c': len(c_list),
        'd': len(d_list),
        'e': len(e_list),
        'f': len(f_list),
        'g': len(g_list),
        'h': len(h_list),
        'i': len(i_list),
        'j': len(j_list),
        'k': len(k_list),
        'l': len(l_list),
        'm': len(m_list),
        'n': len(n_list),
        'o': len(o_list),
        'p': len(p_list),
        'q': len(q_list),
        'r': len(r_list),
        's': len(s_list),
        't': len(t_list),
        'u': len(u_list),
        'v': len(v_list),
        'w': len(w_list),
        'x': len(x_list),
        'y': len(y_list),
        'z': len(z_list),
    }

    return word_list


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
    with open("data/words.json", 'w+') as f:
        f.write(content)
        print('file write successful!')


if __name__ == '__main__':
    words = get_words()
    print(words)
    # write_file(json.dumps(words))
