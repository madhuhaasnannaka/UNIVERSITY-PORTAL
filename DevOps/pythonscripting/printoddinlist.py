odd=[]
values=[]
x=input()
values=x.split(",")
for i in values:
    if (int(i)%2!=0):
        odd.append(i)

print(",".join(odd))

