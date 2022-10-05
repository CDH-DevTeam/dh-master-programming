sample_text = """
            Sorlar sorlar, susar
            sommarregnets sorl,
            alla trädens våta
            blad ock knoppar gråta
            dropp - dropp - dropp
            och därnedan rusar
            bäck i sorl och porl
            bäck i sorl.
            """


def write_text_file(text, path):

    with open(path, "w") as f:
        f.write(text)


def read_text_file(path):

    with open(path, "r") as f:
        text = f.read()

    return text

def get_n_characters_of_text(text):

    counter = 0
    for char in text:
        counter += 1

    return counter

def get_n_words_of_text(text):

    word_list = text.split(" ")

    n_words = len(word_list)

    return n_words