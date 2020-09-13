# #hiding a messege in another messege
# #project 2
# def encode():
#     #convert char to binary
#     messege_to_hide = 'hello'
#     x[5] ='hello'
#     for i in messege_to_hide:
#         x[i] = ord(i)
#         print(x[i])
#
# encode()

#def decode(b):
    #convert binary to char
def chapter_entry(title,ch_num,pg_num):
    ''' prints formatted
        chapter chapter_entry
    '''
    left = f"Chapter {ch_num:02d}: {title}"
    return f"{left:.<45s}{pg_num:.>5d}"

print(chapter_entry("something intersting",1,1))

help(chapter_entry)



'''
>>> value =123456
>>> value
123456
>>> f"{value:b}"
'11110001001000000'
>>> f"{value:o}"
'361100'
>>> f"{value:x}"
'1e240'
>>> f"{value:#x}"
'0x1e240'
>>> f"{value:#040_b}"
'0b000_0000_0000_0001_1110_0010_0100_0000'
>>> f"{value:#_b}"
'0b1_1110_0010_0100_0000'
>>> f"{value:#040_b}"
'0b000_0000_0000_0001_1110_0010_0100_0000'
>>> f"{value:#050_b}"
'0b000_0000_0000_0000_0000_0001_1110_0010_0100_0000'
'''
