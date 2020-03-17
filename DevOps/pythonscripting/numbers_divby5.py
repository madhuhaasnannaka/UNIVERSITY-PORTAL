num=[]
num1=[]
read=input()
num=read.split(",")
for i in num:
    nump=int(i,2)
    if (int(i)%5==0):
        num1.append(i)
    

print(",".join(num1))
