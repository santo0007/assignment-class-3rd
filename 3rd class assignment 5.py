lst1 = []
lst2 = []
print("for list number 1:")
n = int(input("enter number of element : "))
for i in range(0, n):
    ele = int(input())

    lst1.append(ele)
print(lst1)

print("for list number 2:")
n = int(input("enter number of element : "))
for i in range(0, n):
    ele = int(input())

    lst2.append(ele)
print(lst2)

a = set(lst1)
b = set(lst2)

if (a.intersection(b)):
    print("True")
else:
    print("False")