#tarea taller 04/03/2018
def p1(n1,n2):
	x=n1
	y=n2
	negativo=False
	l1=[]
	l2=[]
	result=0
	if x == 0 or y==0:
		print("El resultado es--> 0")
	else:
		if x<0 or y<0:
			negativo= True
		while x!=0:
			l1=l1+[x]
			l2=l2+[y]
			x=int(x/2)
			y=y*2
		print(l1,l2)
		for i in range(0,len(l1)):
			if (l1[i]%2)==1:
				result+=l2[i]
				#print ("gohuer",l1[i])
		if negativo:
			result=result*(-1)
		print("Resultado de multiplicacion-->",result)
p1(90,3)
p1(,)
p1(,)
p1(,)
