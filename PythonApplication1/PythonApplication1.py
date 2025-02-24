from random import randint

print("Hello world from Visual Studio")

s = "*" * 30
print(s)
print("New project")
print(s)



max_number = 0
i = 0
while i<4:
    try:
        number = int(input("¬ведите {0} число: ".format(i+1)))
    except:
        print("¬ы ввели не число")
        exit()
    if (number % 2 == 0) and (number > max_number):   
        max_number = number
    i += 1
    # определение четности и перенос этого числа в переменную
if max_number == 0:     
    print("not found")
    # вывод если отсутствует четное число
else:
    print("Ќаибольшее четное число:", max_number)
    # вывод наибольшего четного числа