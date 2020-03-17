t=(1,2,3,4,5,6,7,8,9,10)
tp1=t[5:]
tp2=t[:5]
print(tp1)
print(tp2)


li=list()
for i in t:
    if int(i)%2==0:
        li.append(i)


tp3=tuple(li)
print(tp3)
