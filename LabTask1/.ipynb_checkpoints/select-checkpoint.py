import sys

def main():

    file = open(sys.argv[1], "r")
    line = [i.strip() for i in file.readlines()]
    
    for i in sys.argv[2:]:
        print(line[int(i)-1])

main()