def addlist(list):
    sum=0
    if len(list)==1:
         return list[0]
    else:
        return list[0]+ addlist(list[1:])
    

print(addlist([1,2,3,4]))
