def fibo(N):
	a, b = 0, 1
	for _ in range(N):
		a, b = b, a+b
	return a

if __name__=="__main__":
	print "Fibo(5)" + str(fibo(5))
	