import csv

with open("attendance.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["EmpID","Name","Status"])
    writer.writerow([1, "Amit", "Present"])
    writer.writerow([2, "Riya", "Absent"])

with open("attendance.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

with open("attendance.csv","a",newline="") as f:
    writer=csv.writer(f)
    writer.writerow([3,"Karan","Present"])

count=0
with open("attendance.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        if row["Status"]=="Absent":
            count += 1

print("Absent employees:",count)

eid=input("Enter employee ID:")

with open("attendance.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        if row["EmpID"]==eid:
            print(row)
