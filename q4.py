text=input("Enter text: ")
other_charcter=0
upper_case=0
lower_case=0
digit=0
spaces=0
for i in text:
    if i.isdigit():
        digit+=1
    elif i.isupper():
        upper_case+=1
    elif i.islower():
        lower_case+=1
    elif i.isspace():
        spaces+=1
    else:
        other_charcter+=1
print(f"Digits: {digit}")
print(f"Upper case: {upper_case}")
print(f"Lower case: {lower_case}")
print(f"Spaces: {spaces}")
print(f"Other charcters: {other_charcter}")
