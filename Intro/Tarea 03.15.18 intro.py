def largo(x):
    cont = 0
    while x > 0:
        cont += 1
        x = x // 10
    return cont
def ejer(x,y):

	if largo(y)!=largo(x):
		return -1
	Lx = []
	Ly = []
	while x!=0:
		digitX = x%10
		digitY = y%10
		Lx=[digitX]+Lx
		Ly=[digitY]+Ly
		x//=10
		y//=10
	
	Lres = []
	#print(Lx)
	cont = 0

	print("Sin destruir - While")
	while cont < len(Lx):
		digitX = Lx[cont]
		digitY = Ly[cont]
		Lres+=[digitX+digitY]
		cont+=1
	print(Lres)
	LxTemp= Lx
	LyTemp= Ly
	Lres = []
	print("Destruyendo - While")
	while len(Lx)>0:
		digitX = Lx[0]
		digitY = Ly[0]
		Lx=Lx[1:]
		Ly=Ly[1:]
		Lres+=[digitX+digitY]
	print(Lres)	


	#RECUPERAR LAS LISTAS DESTRUIDAS
	Lx=LxTemp
	Ly=LyTemp

	Lres=[]

	print("For item in L")
	for item in Lx:
		Lres += [item]
	
	cont = 0
	for item in Ly:
		Lres[cont] += item
		cont+=1

	print(Lres)


	Lres=[]
	print("For i in range")
	for hanzo in range(0,len(Lx)):
		Lres+=[Lx[hanzo]+Ly[hanzo]]
	print(Lres)
	
	return 0


res = ejer(192835,346781)

if res>=0:
	print("Ejecucion exitosa")
else:
	print("Hubo un error")