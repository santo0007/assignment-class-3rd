lst1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst1.append(ele)

print(lst1)

print(list(set(lst1)))