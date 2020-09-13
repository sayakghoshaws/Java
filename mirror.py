import sys
##mirroring function
def mirror(file):
    '''Print the line of the file, flipped right to left'''
    for line in file:
        print(line[::-1])

## main functions
def main():
    ##get the single argument,the filename itself
    name = sys.argv[1]

    ##just mirror that file
    with open (name) as f:
        mirror(f)

##runs
main()
