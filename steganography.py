#Student Name           :Sayak Ghosh
#ID                     :873464327
#Description of Program :This python program takes a messege from user
#                        and encodes and then decodes it.
#######################################################################
# import statements for this program
import string
#######################################################################
#function definitions used in this program

def show_output(secret_msg,secret_msg_ascii,secret_msg_binary,display_binary,hidden_string):
        #This function is just to seperate out the print functions,which can be disabled later
        '''This is a function to display the output of encode function'''

        print('original input messege :',secret_msg,'\n')
        print('ascii conveted messege :',secret_msg_ascii)
        print('binary conveted messege:',secret_msg_binary,'\n')
        print('aligned message  :',display_binary)
        print('hidden message   :',hidden_string,'\n')

def encode(secret_msg = 'hello!!!',masking_string = 'a'*100):
    '''This function takes user character input and a
       masking string and hides it into the masking string
       1)secret_msg first argument is the messege you want to encode
       2)masking_string second argument is the messege in which you wants
                      hide the secret messege into'''

    #declare variables used in this function
    secret_msg_ascii = ''
    secret_msg_binary = ''
    hidden_string = ''
    display_binary = ''
    mask_str_idx = 0
    secret_msg_idx = 0

    #below code coverts the user intput into ascii & binary string and adds null
    secret_msg = f"{secret_msg}\0"
    for i in range(0,len(secret_msg)):
        secret_msg_ascii += f"{ord(secret_msg[i]): 7d} "
        secret_msg_binary += f"{ord(secret_msg[i]):07b} "

    #Error handling for correct user input
    if len(secret_msg_binary)>len(masking_string):
        print('Please enter a longer masking string and rerun or don\'t use the masking string')
        return ''

    #below code hides the secret msg from user inside masking string
    while mask_str_idx < len(masking_string) and secret_msg_idx < len(secret_msg_binary):
        if masking_string[mask_str_idx] in string.ascii_letters:
                if secret_msg_binary[secret_msg_idx] == '1':
                    hidden_string += str.upper(masking_string[mask_str_idx])
                    display_binary += secret_msg_binary[secret_msg_idx]
                    secret_msg_idx += 1
                    mask_str_idx += 1
                elif secret_msg_binary[secret_msg_idx] == '0':
                    hidden_string += str.lower(masking_string[mask_str_idx])
                    display_binary += secret_msg_binary[secret_msg_idx]
                    secret_msg_idx += 1
                    mask_str_idx += 1
                else:
                    secret_msg_idx += 1
        else:
            hidden_string += str.lower(masking_string[mask_str_idx])
            mask_str_idx += 1
            display_binary += ' '
    #append the remaining string which is not processed by the loop above
    hidden_string += str.lower(masking_string[mask_str_idx:])
    #show_output(secret_msg,secret_msg_ascii,secret_msg_binary,display_binary,hidden_string)
    return hidden_string

def decode(hidden_string):
    '''This function takes hidden string from encode() or user and converts
       it back to original messege'''
    #check if the encoded messege is valid
    if hidden_string == '':
        return 'Nothing to decode,Check your secret msg or masking string'

    #declare variables used in this function
    decoded_binary_msg =''
    start = 0
    binary_decoded_string =''

    #take input from encoded function and decode the hidden secret msg
    for c in hidden_string:
        if c in string.ascii_letters:
            if str.isupper(c):
                decoded_binary_msg += '1'
            else:
                decoded_binary_msg += '0'
    while start <= len(decoded_binary_msg):
        binary_decoded_string += chr(int(decoded_binary_msg[start:start + 7],2))
        start += 7
    #print('decoded message  :',binary_decoded_string)
    return binary_decoded_string

#######################################################################
#call functions defined above
decode(encode('it\'s me','This is a perfectly normal sentence.Nothing interesting to see here.'))

######################################################################
#####################End of Code######################################
