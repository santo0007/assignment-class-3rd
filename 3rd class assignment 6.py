lst = []
count = 0
n = int(input("Enter number of element : "))
for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print(lst)

a = int(input())
for i in range(0, len(lst)):
    if a ==lst[i]:
        count = count+1
print(count)