#работа с условными операторами

num = int(input("Введите число: "))

if num % 2 == 0:
	print("Число чётное")
else:
	print("Число нечётное")
	
if num>0:
	print("Число положительное")
elif num<0:
	print("Число отрицательное")
else:
	print("Число равно нулю")
