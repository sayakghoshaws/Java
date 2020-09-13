# #list are dependent on sequences
# #random  access
# #empty collection
# phonebook ={}
# #or phonebook = dict()
#
# ##specifying values
# #phonebook['Alice']='12345678'
# ##specifying values
# d = {
#     ##key:value,
#     'Alice':'555-5555',
#     'Bob' : '666-6666',
#     'Charlie' : '777-777'
# }
#
# ##specifying pairs works the same way
# # d = dict ([
# #     ##key:value,
# #     ('Alice':'555-5555'),
# #     ('Bob' : '666-6666'),
# #     ('Charlie' : '777-777')
# # ])
#
# ##keys can be anything which needs to be hashable
# ##you can change values ,assign values and delete them
# a = d['Bob']
# print(a)
#
# d['Bob'] = '111-111'
# print(d['Bob'])
#
# # del d['Bob']
# # print(d['Bob']) #key error
#
# d['Bob'] = d['Alice']
# print(d['Bob'])
#
# for number in d.values():
#     print(number)
#
# for name in d.keys():
#     print(name)
#
# for name in d:
#     print(name)  #just keys default
#
# if 'Bob' in d:
#     print("Bob's number is ",d['Bob'] )
#
#
# #partition by word length
# def words_by_length(words):
#     '''Returns a dictionary mapping lengths to lists of words of that length'''
#     lengths_dict ={}
#
#     for word in words:
#          length = len(word)
#          if length is lengths_dict:
#              #length is already a key so thre is already a list we don't want
#              #to overwrite it  but we want to extend it.
#              lengths_dict[length] += [ word ]
#          else:
#              lengths_dict[length]
#
#     print(lengths_dict)
#     return length_dict
#
# words_by_length('sfasda dafafa dfasfaf')


def reverse_map(string):
    '''Returns a dictionary from characters
    to their indices'''
    #long way
    # d = {}
    # for idx, c in enumerate(string):
    #     d[c] = idx
    # return(d)
    #short way with dictionary comprehensions
    print({ c:idx for idx, c in enumerate(string) if idx%2 == 0}) #{'a': 0, 'b': 1, 's': 2, 'f': 3, 'e': 7, 'w': 5, 'r': 6}
    return { c:idx for idx, c in enumerate(string)}

reverse_map('absfewre')


def reverse_dict(d):
    '''Returns a dictionary mapping lengths to lists of sequences of that length'''
    return {v:k for k,v in d.items()}

reverse_dict(reverse_map('absfewre'))


def unscramble(string,rev):
    '''unscrambles a string using the given dictionary.'''
    return ''.join(rev[c] if c in rev else c for c in string)
