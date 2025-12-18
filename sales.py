import csv

with open("sales.txt","w") as f:
    f.write("01-01-25,500\n")
    f.write("02-01-25,800\n")

with open("sales.txt","a") as f:
    f.write("03-01-25,600\n")

with open("sales.txt","r") as txt,open("sales.csv","w",newline="") as csvf:
    writer=csv.writer(csvf)
    writer.writerow(["Date","Amount"])

    for line in txt:
        writer.writerow(line.strip().split(","))

with open("sales.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

total=0

with open("sales.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["Amount"])

print("Total sales:",total)