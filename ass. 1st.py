a = int(input("Enter the value:"))
if a<100 and a>80:
   print("Your grade is A+")
elif a>=75 and a<=79:
    print("Your grade is not A")
elif a>=70 and a<=74:
    print("Your grade is not A-")
elif a>=65 and a<=69:
    print("Your grade is not B+")
elif a>=60 and a<=69:
    print("Your grade is not B")
elif a>=55 and a<=59:
    print("Your grade is not B-")
elif a>=50 and a<=54:
    print("Your grade is not C+")
elif a>=45 and a<=49:
    print("Your grade is not C")
elif a >= 40 and a <= 44:
    print("Your grade is not D")
elif a>=00 and a<=39:
    print("Your grade is not F")
else:
    print("not grade")
