#######################################################################
#Student Name           :Sayak Ghosh
#ID                     :873464327
#Description of Program :Count bigrams
#######################################################################
def count_bigrams(text):
    words = text.split(' ')
    bigram={}
    for each in words:
        for start in range(len(each)-2):
            bigram_key =str.lower(each[start:start+2])
            if bigram_key in bigram:
                count = bigram[bigram_key]
                bigram[bigram_key] = count +1
            else:
                bigram[bigram_key] = 1
    print(bigram)
    return bigram
