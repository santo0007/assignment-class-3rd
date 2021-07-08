list =[]
n = int(input("Enter number of elements in list:"))
for i in range(0, n):
    ele = int(input("Enter elements:"))
    list.append(ele)
print(list)

    list.sort()
    print("largest element is:", list[-1])