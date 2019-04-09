from vocab_file_parser import *

files = ['list_a', 'list_b', 'list_c', 'list_d', 'list_e']


def main():
    definitions = word_list(files)
    keys = sorted(definitions.keys())
    for word in keys:
        print("{} => {}".format(word, definitions[word]))


if __name__ == '__main__':
    main()
