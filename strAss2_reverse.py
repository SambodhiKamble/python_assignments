s=input("Enter a string")

words=s.split()
result=[word[::-1] for word in words]

print(result)