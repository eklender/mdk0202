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
        number = int(input("������� {0} �����: ".format(i+1)))
    except:
        print("�� ����� �� �����")
        exit()
    if (number % 2 == 0) and (number > max_number):   
        max_number = number
    i += 1
    # ����������� �������� � ������� ����� ����� � ����������
if max_number == 0:     
    print("not found")
    # ����� ���� ����������� ������ �����
else:
    print("���������� ������ �����:", max_number)
    # ����� ����������� ������� �����