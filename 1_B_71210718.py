input1 = int(input("Masukkan banyak bilangan : "))
i=1
print("Total = ", end="")

for x in range(1, input1 + 1):
    if x % 7 ==0:
        i=i + 0
    elif x % 3 == 0:
        i=i + (x * -1)
        print("- " + str(x), end= " ")
    elif x==1 :
        print(str(x), end=" ")
    else:
        i= i + x
        print("+ " + str(x), end=" ")
print("\nHasil perhitungan diatas ialah " + str(i))