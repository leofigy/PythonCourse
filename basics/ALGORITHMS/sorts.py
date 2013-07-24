def Bubblesort(x=[]):
	swap = True
	while swap:
		swap = False
		for i in range(len(x)-1):
			if x[i]>x[i+1]:
				tmp = x[i]
				x[i] = x[i+1]
				x[i+1] = tmp
				swap = True


x = [9, 4, 5, 9, 32]
print x
Bubblesort(x)
print x
