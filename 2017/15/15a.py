A = 699
B = 124

A_list = []
B_list = []
count = 0

for i in range(4*(10**7)):
	new_A = (A*16807)%2147483647
	new_B = (B*48271)%2147483647
	if bin(new_A)[-16:] == bin(new_B)[-16:]:
		count += 1
	A = new_A
	B = new_B
	if i%100000 == 0:
		print(i)
print(count)