# import module for using command line arguments to pass input into python
import sys

def main():

    # open file and convert convert blabla
    list1 = open((sys.argv[1]), "r")
    list2 = open((sys.argv[2]), "r")

    # put into set for easy intersection command
    str_1 = set([int(line.strip()) for line in list1.readlines()])
    str_2 = set([int(line.strip()) for line in list2.readlines()])

    # ya print
    print("Overlap is", str_1.intersection(str_2))

main()