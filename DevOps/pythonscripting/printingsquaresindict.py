def pdict():
    dict={}
    li=list()
    for i in range(1,21):
        dict[i]=i**2
        li.append(dict[i])
    print(li[15:20])
    
pdict()
