A = 699
B = 124

A_list = []
B_list = []
count = 0
def gen_A(A):
	A = (A*16807)%2147483647
	while A % 4 != 0:
		A = (A*16807)%2147483647
	return A

def gen_B(B):
	B = (B*48271)%2147483647
	while B % 8 != 0:
		B = (B*48271)%2147483647
	return B

for i in range(5*(10**6)):
	new_A = gen_A(A)
	new_B = gen_B(B)
	if bin(new_A)[-16:] == bin(new_B)[-16:]:
		count += 1
	A = new_A
	B = new_B
	if i%100000 == 0:
		print(i)
print(count)