import sys
def main():
    try:
        file = open(sys.argv[1], "r")
        line = [i.strip() for i in file.readlines()]
    
        free = list()
        for i in sys.argv[2:]:
            free.append(line[int(i)-1])

        for j in free:
            print(j)
    except FileNotFoundError as fe:
        print("Unable to read from file:", fe)       
        
    except ValueError as ve:
        print("Invalid line number specified:", ve)
    
main()

