values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
new_list=[]
for i in values:
    if i not in new_list:
        new_list.append(i)
print(new_list) 