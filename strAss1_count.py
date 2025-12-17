s=input("Enter string:")

v=c=d=sp=0

for ch in s:
    if ch.lower()  in "aeiou":
        v+=1

    elif ch.isalpha():
        c+=1

    elif ch.isdigit():
        d+=1

    else:
        sp+=1

print("Vowels:",v)
print("Consonants:",c)
print("Digits",d)
print("Special characters:",sp)