A = input()

b=A

c=d=0

c=A.find('not')
d=b.find('poor')

if(c>0 and d>=0):
    b= b.replace(b[c:d+4],'good')
    print(b)