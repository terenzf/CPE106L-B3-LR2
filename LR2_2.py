fileInput = input("Enter a file name: ")
file = open(fileInput, 'r')
lineCounter = 0

for line in file:
    lineCounter = lineCounter + 1

print("There are", lineCounter, "lines in this file")

while True:
    lineNumber = 0

    num = int(input("Enter a line number (0 to quit): "))
    if num >=1 and num <= lineCounter:
        file = open(enterfile, 'r')
        for lines in file:
            lineNumber = lineNumber + 1
            if lineNumber == num:
                print(lines)
    else:
        if num == 0:
            print("The program has been terminated. Thank you.")
            break
