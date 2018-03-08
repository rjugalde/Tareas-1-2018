def largo(x):
    cont = 0
    while x > 0:
        cont += 1
        x = x // 10
    return cont


def p1(x, y):
    larx = -1
    lary = -1
    pares = 0
    impares = 0
    cont = 0
    result = 0
    res1 = 1
    res2 = 0
    if larx != lary:
        print("Los numeros son de distinta longitud")
    else:
        temp1 = x
        temp2 = y
        while (temp1 > 0):
            if (temp1 % 10) % 2 == 0:
                larx += 1
            else:
                lary += 1
            temp1 //= 10
        while (temp2 > 0):
            if (temp2 % 10) % 2 == 0:
                larx += 1
            else:
                lary += 1
            temp2 //= 10
        while x > 0:
            X = x % 10
            Y = y % 10
            print(X, Y)
            print(pares, impares)
            if X % 2 == 0:
                pares = pares + (X * 10**(larx))
                larx -= 1
            if X % 2 == 1:
                impares = impares + (X * 10**(lary))
                lary -= 1
            if Y % 2 == 0:
                pares = pares + (Y * 10**(larx))
                larx -= 1
            if Y % 2 == 1:
                impares = impares + (Y * 10**(lary))
                lary -= 1
            x = x // 10
            y = y // 10
    mayor = impares
    if pares > impares:
        mayor = pares
    while mayor > 0:
        X = pares % 10
        Y = impares % 10
        T = X + Y
        if T > 9:
            result = result + T * (10**cont)
            cont += 1
        else:
            result = result + T * (10**cont)
        cont += 1
        pares = pares // 10
        impares = impares // 10
        mayor = mayor // 10
        print(result)
    temp = result
    while (temp > 0):
        if (temp % 10) % 2 == 0:
            res1 *= temp % 10
        else:
            res2 += temp % 10
        temp //= 10
    print("Suma impares-->", res2)
    print("Mult pares-->", res1)
def p2(x):
	result=0
	while x>0:
		b= x%10
		if b>result:
			result=b
		x=x//10
	print("El digito mas alto es-->",result)
p1(41234, 86138)
p2(612378)