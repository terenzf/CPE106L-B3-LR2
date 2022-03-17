"""
File: mean.py
Prints the mean of a set of numbers in a file.
"""

fileName = input("Enter the file name: ")   # Input fileName
f = open(fileName, 'r')                     # Open the file in read mode

sum=0       # Initialize sum to 0
count=0     # Initialize count to 0

for line in f.readlines():  # For each line in file
    sum+=float(line.strip())    # Add the number to sum
    count+=1                    # Increment count by 1
print ('The Mean is:', (sum/count)) # Outputs the Mean (Average)




