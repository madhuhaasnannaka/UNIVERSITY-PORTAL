li=[1,2,3,4,5,6,7,8,9,10]
evennumber1=filter(lambda x:x%2==0,range(1,21))
print(evennumber1)

sqares=map(lambda x:x**2,filter(lambda x:x%2==0,li))
print(map(lambda x:x**2,filter(lambda x:x%2==0,li)))


class American(object):
    @staticmethod
    def printNationality():
        print("America")
anAmerican = American()
anAmerican.printNationality()
American.printNationality()
