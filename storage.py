#######################################################################
#Student Name           :Sayak Ghosh
#ID                     :873464327
#This program saves and loads a valiable into a file with its type
#######################################################################
#define a user defined exception which we can raise if the value type doesn't
#match declared type
class ImproperFileFormat(Exception):
    pass

a = ['this', 'is', 'a', 'something', 1, 2, 3, 4,2.0,['x',['nested','lst']]]
#a = [1,'string',['x','y']]
#a = [1, 2, 'hello', 'goodbye', 10.1, 20.2]
b = 300.0
f = ''

def save(f,a):
    '''takes filename f and variable to store as a in argument and stores them in
    storage.txt file'''
    # if the variable is not of type list then don't use loop
    if type(a) in (str,int,float):
        if type(a) == str:
            type_flag = 'S'
        elif type(a) == int:
            type_flag = 'I'
        elif type(a) == float:
            type_flag = 'F'
        else:
            raise ImproperFileFormat
        f.write(f'{type_flag} {a}\n')
        return
    elif type(a) == list:
        type_flag = 'L'
        f.write(f'{type_flag} {len(a)}\n')


    #check the type of element in the given variable and set first character of
    #accordingly
    for element in a:
        if type(element) == str:
            type_flag = 'S'
        elif type(element) == int:
            type_flag = 'I'
        elif type(element) == float:
            type_flag = 'F'
        elif type(element) == list:
            type_flag = 'L'
        else:
            raise ImproperFileFormat(f'{element}')
    #write file with type as first character followed by value
    #for list call recursion by calling list element
        if type_flag == 'L':
            current_list_item = element
            save(f,element)
        else:
            f.write(f'{type_flag} {element}\n')
            #f.flush()
            #print(f'{type_flag} {element}')

def load(f):
    '''takes filename f and loads the content into variable'''
    #check the type of element in the given variable and set first character of
    #accordingly
    lst_to_store =[]
    for line in f:

        line = line.strip()

        if line[0] == 'S':
            return line[2:]
        elif line[0] == 'I':
            return int(line[2:])
        elif line[0] == 'F':
            return float(line[2:])
        elif line[0] == 'L':
            nested_lst=[]
            for idx in range(0,int(line[2:]),1):
                nested_lst.append(load(f))
            lst_to_store+=nested_lst
            nested_lst=[]
    return lst_to_store

#call the save functions inside try catch block
try:
    with open ('for-later.txt',mode='w',encoding='utf-8') as f:
        save(f,a)
        #save(f,b)

    with open ('for-later.txt',mode='r',encoding='utf-8') as f:
        print(load(f))


except FileNotFoundError:
    print('File Not Found!!!')
except ImproperFileFormat as error:
    print('the value does not match type mentioned',str(error))
