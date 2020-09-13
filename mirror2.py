import sys
##mirroring function
def mirror(file):
    '''Print the line of the file, flipped right to left'''
    for line in file:
        print(line[::-1])

## main functions
def main():
    ##check if we have a name
    if len(sys.argv) >= 2
        ##get the single argument,the filename itself
        name = sys.argv[1]
        ##just mirror that file
        with open (name) as f:
            mirror(f)
    else:
        ##we have nothing
        mirror(sys.stdin)
##runs
main()
