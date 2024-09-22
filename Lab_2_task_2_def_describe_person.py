name = str(input())

def describe_person(name, age = 30):
	c = "Меня зовут "
	b = ", "
	a = "мне "
	age = str(age)
	e = " лет"
	return c+name+b+a+age+e
print(describe_person(name, age = 30))
