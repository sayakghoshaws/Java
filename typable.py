def typeable(keys,words):
        '''Return words which contain only letters in keys.'''
        #set is not bothered about order
        keyset = set(keys)
        return [word for word in words if set(word)<=keyset]

def longest_words_single_pass():
    '''returns the longest word of a list'''
    longest= [wordlist[0]]
    for word in wordlist:
        if len(word)==len(longest[0])
            longest += [word]
        elif len(word) > len(longest[0]):
            longest =[word]
        return longest
