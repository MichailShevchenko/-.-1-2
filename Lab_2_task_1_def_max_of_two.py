x = int(input())
y = int(input())
def max_of_two(x, y):
	if x>y:
		return x
	if y>x:
		return y
.       if y==x:
.               return "Числа равны"
print(max_of_two(x, y))
