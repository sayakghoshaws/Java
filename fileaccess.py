##two ways stream and Random access
##read or write in entirity for stream

#how to open a file
#mode r ,w a
# #read,write(overwrite),append(towards the end)
# f = open('test.txt',mode='w',encoding='utf-8')

#with automatically closes the file even in case of an exception
# with open ('messege.txt',mode='r') as f:
#     print(f.read())

new_msg = input("Enter New Messege: ")
with open ('messege.txt',mode='w',encoding='cp037') as f:
    f.write(new_msg)

# with open ('messege.txt',mode='r') as f:
#     list =[]
#     for line in f:
#         list+= [int(line)]
#         #list.append(int(line))

#list = [in(line) for line in f]
