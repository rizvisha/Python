s = '        asd   d    \n\n    asd       asd '
poem_lines = ['The first line leads off,', 'With a gap before the next.','Then the poem ends.']
word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'], 'GAP':
                    ['G', 'AE1', 'P'], 'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                    'LEADS': ['L', 'IY1', 'D', 'Z'], 'WITH': ['W', 'IH1', 'DH'],
                    'LINE': ['L', 'AY1', 'N'], 'THEN': ['DH', 'EH1', 'N'],
                    'THE': ['DH', 'AH0'], 'A': ['AH0'], 'FIRST':
                    ['F', 'ER1', 'S', 'T'], 'ENDS': ['EH1', 'N', 'D', 'Z'],
                    'POEM': ['P', 'OW1', 'AH0', 'M'], 'OFF': ['AO1', 'F']}
pattern = ([5, 7, 5], ['A', 'B', 'A'])

def get_poem_lines(string):
    clean_list = []
    lst = string.splitlines()
    for line in lst:
        if line != '':
            lst_f.append(line.strip())
    return clean_list

def count_vowel_phonemes(lst):
    counter = 0
    for element in lst:
        for char in element:
            if char.endswith('0') or char.endswith('1') or char.endswith('2'):
                counter += 1
    return counter

def last_phonemes(lst):
    phonemes = []
    i = len(lst) - 1
    c = i
    while i >= 0:
        if lst[i].endswith('0') or lst[i].endswith('1') or lst[i].endswith('2'):
            while i <= c:
                phonemes.append(lst[i])
                i +=1
            return phonemes
        i -= 1
    return phonemes

#HELPER============FUNCTIONS========

def clean_up(s):
    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result

def list_of_lines(lst):
    """Return list of list of words such that words in one line are in one list.
    """
    l = []
    for char in lst:
        l.append(char.split())
    return l

def list_of_lines_clean(lst):
    """Return the cleaned list of list of words.
    """
    lst1 = []
    for element in lst:
        lst2 = []
        for word in element:
            lst2.append(clean_up(word))
        lst1.append(lst2)
    return lst1

def num_of_vowel(lst, dic):
    """Return a list with number of phonemes per line as elements"""
    num_vowels = []
    for element in lst:
        total = 0
        i = 0
        while i < len(element):
            j = 0
            while j < len(dic[element[i]]):
                if '0' or '1' or '2' in dic[element[i]][j]:
                    total += 1
                j += 1
            i += 1
        num_vowels.append(total)
    return num_vowels

def is_equal(num_vowels, pattern):
    """Return the lines which have incorrect number of phonemes."""
    result = []
    i = 0
    if num_vowels[i] != pattern[0][i]:
        result.append(poem_lines[i])
    return result      

def pattern(lst):
    i = 0
    while i < len(pattern[1]):
        if pattern[1][i] == 'A':
            A.append(i)
        elif pattern[1][i] == 'B':
            B.append(i)
        elif pattern[1][i] == 'C':
            C.append(i)
            
#=========================================
            
def phoneme_lst(clean_lst):
    phoneme_lst = []
    for lst in clean_lst:
        word = lst[len(lst) - 1]
        rhyme_pattern = last_phonemes(word_to_phonemes[word])
        phoneme_lst.append(rhyme_pattern)
    return phoneme_lst


def dic(pattern):
    d = {}
    counter = 0
    for ch in pattern[1]:
        if ch not in d:
            d[ch] = [counter]
        else:
            d[ch].append(counter)
        counter += 1
    return d

def lines_not_rhyming(dic):
    not_rhyming = []
    for value in dic.values():
        #if value != *
        i = 0
        temp = rhymes[value[0]]
        while i < len(value):
            if rhymes[value[i]] != temp:
                j = 0
                while j < len(value):
                    not_rhyming.append(poem_lines[value[j]])
                    j += 1
            i += 1
    return not_rhyming

#=========================================#1winnner stands alone, manuscript found
#in ...., aleph, warrior of the light, the #2zahir, #3the witch of portobello.
#the shadow of the crescent moon.

def read_pronunciation(pronunciation_file):
    d = {}
    for line in pronunciation_file:
        if not line.startswith(';;;'):
            lst = line.split()
            d[lst[0]] = []
            i = 1
            while i < len(lst):
                d[lst[0]].append(lst[i])
                i += 1
    return d

def read_poetry_form_descriptions(pronunciation_file):
    d = {}
    for line in pronunciation_file:
        if line[0].isalpha():
            name = line.rstrip('\n')
            d[name] = ([], [])
        elif line != '\n':
            lst = line.split()
            d[name][0].append(lst[0])
            d[name][1].append(lst[1])
    return d
        
#Checks that the indices of the poem at each rhyme scheme are rhyming
    #and makes a list of the lines that should rhyme, but dont.
    #Assign this list to result.
    
    #result = lines_not_rhyming(rhyme_dictionary)
    #return result      
            
#===========================================            
