import sys

## function to break up the text
def break_lines(file,width):
    '''Prints lines from file,inserting newlines to make sure each line has
    at most  width characters'''
    for line in file:
        chars_per_line = 0
        for word in line.split():
            if chars_per_line == 0:
                print(word,end='')
                chars_per_line = len(word)
            elif chars_per_line + 1 + len(word) > width:
                print()
                print(word,end='')
                chars_per_line = len(word)
            else:
                print(' ',word,sep='',end='')
                chars_per_line += + len(word)

    # for line in file:
    #     while len(line) > width:
    #         print(line[:width])
    #         line  = line[width:]
    #     print(line,end='')

def main():
    name =  sys.argv[-1]

    ##all the other arguments
    args = sys.argv[1:-1]
    i = 0
    while i < len(args):
        ##get the argumanet and compare to known cases
        arg = args[i]
        if arg == '-c':
            width = int(args[i+1])
            i += 1
        else:
            print(f'unrecognized option: {arg}',file=sys.stderr)

    ##process that single file
    with open(name) as f:
        break_lines(f,width)

##call main
main()
