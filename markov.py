from random import choice


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

    full_text_stripped = text_string.replace("\n", " ")

    words = full_text_stripped.split(" ")
    
    for i in range(len(words)- 2):
        # if words[i] == words[-1]:
        #     chains[(words[i])] = ""
        # else:
        key_tuple = (words[i], words[i + 1])
        chains[key_tuple] = ""

    # for key in chains:
    #     if key == "":
    #         del chains[key]
    #         break

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


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

processed_file = open_and_read_file(input_path)

make_chains(processed_file)

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
