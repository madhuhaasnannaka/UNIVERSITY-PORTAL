s=input()
freq={}
for word in s.split():
    freq[word]=freq.get(word,0)+1




words=freq.keys()

for w in sorted(freq.keys()):
    print("%s:%d"%(w,freq[w]))
    
