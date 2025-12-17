import copy

lst=[[1,2],[3,4]]

shallow=lst.copy()
deep=copy.deepcopy(lst)

lst[0][0]=100

print("Original list:",lst)
print("Shallow list:",shallow)
print("Deep list:",deep)