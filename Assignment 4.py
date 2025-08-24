#Task 1
try:
    fileS = open("Sample.txt","r")
    TXT = fileS.readline()
    TXT1 = fileS.readline()
    print("Reading file content:")
    print("Line 1:",TXT)
    print("Line 2:",TXT1)
    fileS.close()
except FileNotFoundError:
    print("The file 'Sample.txt' was not found.")
#Task 2
try:
    file_c = input("Enter text to write to the file: ")
    file_h = open("Output.txt", "w")
    try:
        file_h.write(file_c+'\n')
        print("Data successfully written to Output.txt")
    finally:
        file_h.close()
    add_c = input("Enter additional text to append: ")
    file_h = open("Output.txt", "a")
    try:
        file_h.write(add_c+'\n')
        print("Data successfully appended to Output.txt")
    finally:
        file_h.close()
    file_h= open("Output.txt", "r")
    try:
        print("\nFinal content of Output.txt:")
        print(file_h.read())
    finally:
        file_h.close()
        print("Thank you")
except FileNotFoundError:
    print("The file 'Output.txt' was not found.")
    print("Thank you")







