input1 = int(input("Masukkan angka :"))
for i in range(input1):
	for j in range(input1):
		if i==(input1-1) or j==(input1-1) or i+j==(input1-1):
			print('*', end=' ')
		else:
			print(' ', end=' ')
	print()



