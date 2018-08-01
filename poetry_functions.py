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


# ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


# Add your helper functions here.

def list_of_lines(lst):
    """(list of str) -> list of list of str

    Return list of list of words such that words in one line are in one list.

    >>>list_of_lines(['The first line leads off,', 'With a gap before the
    next.', 'Then the poem ends.'])
    [['The', 'first', 'line', 'leads', 'off,'], ['With', 'a', 'gap', 'before',
    'the', 'next.'], ['Then', 'the', 'poem', 'ends.']]
    """
    
    l = []
    for char in lst:
        l.append(char.split())
    return l

def list_of_lines_clean(lst):
    """(list of list of str) -> list of list of str
    
    Return the cleaned list of list of words.

    >>>list_of_lines_clean([['The', 'first', 'line', 'leads', 'off,'], ['With',
    'a', 'gap', 'before','the', 'next.'], ['Then', 'the', 'poem', 'ends.']])
    [['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], ['WITH', 'A', 'GAP', 'BEFORE',
    'THE', 'NEXT'], ['THEN', 'THE', 'POEM', 'ENDS']]
    """
    
    lst1 = []
    for element in lst:
        lst2 = []
        for word in element:
            lst2.append(clean_up(word))
        lst1.append(lst2)
    return lst1

def num_of_vowels(lst, dic):
    """(list of list of str, dict) -> list of int
    
    Return a list with number of phonemes per line as elements

     >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}

    >>>num_of_vowel([['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], ['WITH', 'A',
    'GAP', 'BEFORE', 'THE', 'NEXT'], ['THEN', 'THE', 'POEM', 'ENDS']],
    word_to_phonemes)
    [5, 6, 5]
    """
    num_vowels = []
    for element in lst:
        total = 0
        i = 0
        while i < len(element):
            for string in dic[element[i]]:
                if string.endswith('0') or string.endswith('1') or \
                   string.endswith('2'):
                    total += 1
            i += 1
        num_vowels.append(total)
    return num_vowels

def phoneme_lst(clean_lst, word_to_phonemes):
    """(list of list of str) -> list of list of str

    Return the last vowel phoneme and the subsequent consonant phoneme(s) in 
    clean_lst.

    >>>phoneme_lst([['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], ['WITH', 'A',
    'GAP', 'BEFORE', 'THE', 'NEXT'], ['THEN', 'THE', 'POEM', 'ENDS']])
    [['AO1', 'F'], ['EH1', 'K', 'S', 'T'], ['EH1', 'N', 'D', 'Z']]
    """
    
    phoneme_lst = []
    for lst in clean_lst:
        word = lst[len(lst) - 1]
        rhyme_pattern = last_phonemes(word_to_phonemes[word])
        phoneme_lst.append(rhyme_pattern)
    return phoneme_lst


def dic(pattern):
    """(poetry pattern) -> dictionary

    Return a dictionary with rhyme scheme as keys and a list of the indices at
    which the same key occurs as its value.

    >>>pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>>dic(pattern)
    {'B': [1], 'A': [0, 2]}
    >>>pattern = ([5, 7, 5, 7, 5], ['A', 'A', 'A', 'B', 'B'])
    >>>dic(pattern)
    {'B': [3, 4], 'A': [0, 1, 2]}
    """
    d = {}
    counter = 0
    for ch in pattern[1]:
        if ch not in d:
            d[ch] = [counter]
        else:
            d[ch].append(counter)
        counter += 1
    return d

# ===================== Required Functions =====================

def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed 
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n' 'With a gap before
    the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    """
    clean_list = []
    lst = poem.splitlines()
    for line in lst:
        if line != '':
            clean_list.append(line.strip())
    return clean_list


def count_vowel_phonemes(phonemes):
    """ (list of list of str) -> int

    Return the number of vowel phonemes in phonemes.

    >>> phonemes = [['N', 'OW1'], ['Y', 'EH1', 'S']]
    >>> count_vowel_phonemes(phonemes)
    2
    """
    counter = 0
    for element in phonemes:
        for char in element:
            if char.endswith('0') or char.endswith('1') or char.endswith('2'):
                counter += 1
    return counter


def last_phonemes(phoneme_list):
    """ (list of str) -> list of str

    Return the last vowel phoneme and subsequent consonant phoneme(s) in 
    phoneme_list.

    >>> last_phonemes(['AE1', 'B', 'S', 'IH0', 'N', 'TH'])
    ['IH0', 'N', 'TH']
    >>> last_phonemes(['IH0', 'N'])
    ['IH0', 'N']
    >>> last_phonemes(['B', 'S'])
    []
    """
    vowel_phonemes = []
    i = len(phoneme_list) - 1
    c = len(phoneme_list) - 1
    while i >= 0:
        if phoneme_list[i].endswith('0') or phoneme_list[i].endswith('1') \
           or phoneme_list[i].endswith('2'):
            while i <= c:
                vowel_phonemes.append(phoneme_list[i])
                i +=1
            return vowel_phonemes
        i -= 1
    return vowel_phonemes


def check_vowel_phoneme_counts(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    vowel phonemes for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of vowel phonemes, return the empty list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_vowel_phoneme_counts(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_vowel_phoneme_counts(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    """

    #Take poem_lines and splits makes a list of list of lines such that each value
    #is the words in that line. Then uses the clean_up function on these lists.
    #Assign this list to clean_lst.
    
    clean_lst = list_of_lines_clean(list_of_lines(poem_lines))

    #Make a list of the number of vowels in each line. This list has the number
    #of vowels at the corrosponding indices of the respective lines.
    #Assign this list to num_vowels.
    
    num_vowels = num_of_vowels(clean_lst, word_to_phonemes)
    
    i = 0
    lst_lines = []
    while i < len(num_vowels):
        if pattern[0][i] != 0: #0 means no requirement of the number of vowels.
            if num_vowels[i] != pattern[0][i]:
                lst_lines.append(poem_lines[i])
        i += 1
    return lst_lines
    
def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) 
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    """

    #Make a list as given by the list_of_lines_clean helper function.
    #Assign this list to clean_lst.
    
    clean_lst = list_of_lines_clean(list_of_lines(poem_lines))

    #Make a list of the last vowel phoneme and subsequent consonant phoneme(s)
    #in each line in the list "clean_lst".
    #Assign this list to rhymes.
    
    rhymes = phoneme_lst(clean_lst, word_to_phonemes)

    #Create a dictionary with the rhyme scheme characters as keys, and
    #a list of the indices at which these characters occur as their values.
    #Assign this dictionary to rhyme_dictionary.
    
    rhyme_dictionary = dic(pattern)

    not_rhyming = []
    for value in rhyme_dictionary.values():
        temp_list = []
        for x in value:
            if x != '*': #'*' means no requirement for rhyme pattern.
                if rhymes[x] != rhymes[value[0]]:
                    for x in value:
                        temp_list.append(poem_lines[x])
        if temp_list != []:
            not_rhyming.append(temp_list)
    return not_rhyming           

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
