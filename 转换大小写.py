t=input()
result=""
for char in t:
    if char.isupper():
        chars=char.lower()
    else:
        chars=char.upper()
    result+=chars
print(result)


