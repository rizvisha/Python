"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of vowel phonemes required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    d = {}
    for line in pronunciation_file:
        if not line.startswith(';;;'):
            lst = line.split()
            d[lst[0]] = [] #The words as keys with [] as values.
            i = 1
            while i < len(lst):
                d[lst[0]].append(lst[i]) #Appending the phonemes.
                i += 1
    return d


def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    d = {}
    for line in poetry_forms_file:
        if line[0].isalpha():
        #Name has all alphabets while vowel phonemes have numeric characters.
            name = line.rstrip('\n')
            d[name] = ([], [])
        elif line != '\n': #Ignore empty lines.
            lst = line.split()
            d[name][0].append(lst[0])#Append the number of vowels.
            d[name][1].append(lst[1])#Append the rhyme scheme.
    return d


