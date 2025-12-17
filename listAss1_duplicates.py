lst=[1,2,3,4,5,2,3,8,5,3]
new_list=[]

for i in lst:
    if i not in new_list:
        new_list.append(i)

print(new_list)