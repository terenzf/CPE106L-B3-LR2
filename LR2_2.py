fileInput = input("Enter a file name: ")

with open(fileInput) as f:
    lines = [line.rstrip() for line in f]

print("There are", len(lines),"lines in this text file.")

while True:
    num = int(input("Enter a line number [0 = quit]: "))

    if num > 0 and num < len(lines) + 1:
        print(lines[num - 1]) 
    elif num == 0:
        print('The program has been terminated. Thank you.')
        break
