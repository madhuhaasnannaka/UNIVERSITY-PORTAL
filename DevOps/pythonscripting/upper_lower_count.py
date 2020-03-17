d={"Uppercase":0,"Lowercase":0}
s=input()
for i in s:
    if i.isupper():
        d["Uppercase"]+=1
    elif i.islower():
        d["Lowercase"]+=1
    else:
        pass

print("uppercase :",d["Uppercase"])
print("lowercase :",d["Lowercase"])
