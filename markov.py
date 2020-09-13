#######################################################################
#Student Name           :Sayak Ghosh
#ID                     :873464327
#Description of Program :the computer can generate a random sentence by
#starting at a word, randomly picking a successor, and repeating the
#process until it runs out of words.
#######################################################################

import random
d={}
def read_file():
    '''this function reads a .txt file with filename from same folder as .py file
    and stores it into variable data'''
    # read File
    filename = "alice-in-wonderland.txt"
    #
    ## open the file for reading , and interpret as utf-8 text data
    with open(filename,mode='r',encoding='utf-8-sig') as f:
        data =f.read()
    return data
    #print(data[1:100])



def add_successors_one(d, text):
    '''this function takes two parameters: a dictionary and a string.
    It should split text into words, and add each word's successors
    to the given dictionary.'''

    d={}
    split_text = text.split()

    for idx in range(len(split_text)):
        if idx == len(split_text) -1:
            d[split_text[idx]] = ' '
            break

        if split_text[idx] in d.keys():
            d[split_text[idx]] += [split_text[idx +1]]
        else:
            d[split_text[idx]] = [split_text[idx +1]]

    #print(d)
    return d

def generate_words_one(d, start, max_words):
    '''that takes three parameters:  a successor dictionary, a string,
    and an integer.  It should return a list of words beginning with
    start and containing at most max_words words.'''
    s = [start]
    next_key = start

    for idx in range(0,max_words-1):
        if next_key in d.keys():
            random_idx =random.randint(0,len(d[next_key])-1)  #random.choice
            s += [d[next_key][random_idx]]
            next_key = d[next_key][random_idx]
    print(' '.join(s))
    return s

def add_successors_two(d, text,n):
    '''this function takes three parameters: a dictionary,a string & number based
    on which the string will be grouped and key of dictionary will be formed.
    It should split text into n words, and add each word's successors
    to the given dictionary.'''

    d={}
    split_text = text.split()
    multi_text =[]
    grouped_list=[]

    #below for loop takes the split text and makes a new list with words grouped
    #by n words
    for idx in range(len(split_text)-n+1):
        for index in range(n):
            multi_text += [split_text[idx + index]]
        grouped_list +=  [tuple(multi_text)]
        multi_text = []
    #print(grouped_list)

    for idx in range(len(grouped_list)):
        if idx == len(grouped_list) -1:
            d[grouped_list[idx]] = ' '
            break

        if grouped_list[idx] in d.keys():
            d[grouped_list[idx]] += [grouped_list[idx +1][-1]]
        else:
            d[grouped_list[idx]] = [grouped_list[idx +1][-1]]

    #print(d)
    return d

def generate_words_two(d, start, max_words):
    '''that takes three parameters:  a successor dictionary, a string,
    and an integer.  It should return a list of words beginning with
    start and containing at most max_words words.'''
    s=[]

    for idx in range(len(start)):
        s += [start[idx]]
    next_key = start

    for idx in range(0,max_words-1):
        if next_key in d.keys():
            random_idx =random.randint(0,len(d[next_key])-1)
            s += [d[next_key][random_idx]]
            s1 = s[(-1)*len(start):]
            next_key = tuple(s1,)
    print(' '.join(s))
    return ' '.join(s)

#Part One:

#add_successors_one(d,"the quick brown fox jumps over the lazy dog")

generate_words_one(add_successors_one(d,"the quick brown fox jumps over the lazy dog"), 'the', 10)
#generate_words_one(add_successors_one(d,read_file()), 'Alice', 20)


#Part Two:
#add_successors_two(d,"the quick brown fox jumps over the lazy dog",2)
generate_words_two(add_successors_two(d,"the quick brown fox jumps over the lazy dog",2), ('quick', 'brown'), 10)
#generate_words_two(add_successors_two(d,read_file(),1), ('Alice',), 20)
