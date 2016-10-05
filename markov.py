#-*- coding: utf-8 -*-

from random import choice
import codecs

input_path = "green-eggs.txt"

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # tex_file = codecs.open(file_path, encoding='utf-8')
    tex_file = open(file_path)
    full_text = tex_file.read()

    return full_text


def make_chains(text_string):
    """Takes input text as string; returns _dictiencoding='utf-8'onary_ of markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # full_text = text_string.replace("\n", "")
    words = text_string.split()

    
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



def lookup(chains, key_tuple):
    text = key_tuple[0]
    while True:   
        try:
            options = chains[key_tuple]
        except KeyError:
            text = text + " " + key_tuple[1]
            break
        value_choice = choice(options)
        key_tuple = (key_tuple[1], value_choice)
        to_print = str(key_tuple[0])
        text = text + " " + to_print
    return text

processed_file = open_and_read_file(input_path)

chains = make_chains(processed_file)

# getting a random tuple to start out
tuple_lookup = build_tuple(chains)


final_text = lookup(chains, tuple_lookup)

if final_text == " ":
    print lookup(chains, tuple_lookup)
else:
    print final_text