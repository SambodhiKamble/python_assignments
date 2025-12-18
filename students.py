with open("Students.txt","w") as f:
    f.write("101,Alice\n")
    f.write("102,Bob\n")

with open("students.txt","r") as f:
    print(f.read())

with open("students.txt","a") as f:
    f.write("103,Charlie\n")

with open("students.txt","r") as f:
    print(len(f.readlines()))

name=input("Enter name to search:")

with open("students.txt","r") as f:
    for line in f:
        if name in line:
            print("Found:",line)