def fibo(N):
	if N<=1:
		return N
	else:
		return fibo(N-1)+fibo(N-2)

if __name__=="__main__":
	print "Fibo(5)" + str(fibo(5))
	