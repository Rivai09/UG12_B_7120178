str1= input("Masukkan nama :")
print("output : ")
length= len(str1)
for i in range(length):
    for j in range(length-i-1):
        print(" ", end=" ")
    for j in range(i+1) :
        print(str1[j], end=" ")
    print()
for i in range(1, length):
    for j in range(i):
        print(" ", end=" ")
    for j in range(length-i):
        print(str1[j], end=" ")
    print()
    