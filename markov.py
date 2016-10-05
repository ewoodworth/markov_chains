from random import choice

input_path = "green-eggs.txt"

TEXT = ""

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    tex_file = open(file_path)
    full_text = tex_file.read()

    return full_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.strip()
    
    for i in range(len(words)- 2):
        key_tuple = (words[i], words[i + 1])
        chains[key_tuple] = ""

    for key in chains:
        values = []
        for i in range(len(words)):
            if words[i] == words[-1] or words[i] == words [-2] or (words[i]) == key:
                continue
            elif (words[i], words[i + 1]) == key:
                values.append(words[i + 2])
            else: 
                continue
            chains[key] = values

    return chains


def build_tuple(chains):
    """ """

    text_string = open_and_read_file(input_path)

    full_text_stripped = text_string.replace("\n", " ")

    words = full_text_stripped.split(" ")

    first_link = choice(words)

    second_link_possibilities = []

    for i in range(len(words) - 1):
        if words[i] == first_link:
            second_link_possibilities.append(words[i + 1])

    if second_link_possibilities == []:
        return
    else:
        second_link = choice(second_link_possibilities)

    key_tuple = (first_link, second_link)
    return key_tuple



def lookup(chains, key_tuple, TEXT):
    try:
        options = chains[key_tuple]
    except KeyError:
        TEXT = TEXT.replace("?", "?\n")
        print TEXT
        return
    value_choice = choice(options)
    new_tuple = (key_tuple[1], value_choice)
    to_print = str(new_tuple[0])
    TEXT = TEXT + " " + to_print
    if new_tuple[1] == "":
        TEXT = TEXT.replace("?", "?\n")
        print TEXT
    else:
        lookup(chains, new_tuple, TEXT)

processed_file = open_and_read_file(input_path)

chains = make_chains(processed_file)

tuple_lookup = build_tuple(chains)

if lookup(chains, tuple_lookup, TEXT) == " ":
    lookup(chains, tuple_lookup, TEXT)
else:
    lookup(chains, tuple_lookup, TEXT)


