#Opening text file.
fileFound = 0
lineCount = 0
while(fileFound != 1):
    try:
        fileInput = input("Enter a file name: ")
        fileName = open(fileInput, "r")
        fileFound = 1
    except FileNotFoundError:
        print("File name not found.\n")

for line in fileName:
    lineCount = lineCount + 1

#Displaying the number of lines in the file.
print("This text file has", lineCount,"lines.")

#Entering a line number.
while True:
    lineNumber = 0

    num = int(input("Enter a line number (0 to quit): "))
    if num >=1 and num <= lineCount:
        file = open(fileInput, 'r')
        for lines in file:
            lineNumber = lineNumber + 1
            if lineNumber == num:
                print(lines)
    else:
        if num == 0:
            print("The program has been terminated. Thank you.")
            break