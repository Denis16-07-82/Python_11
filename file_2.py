# Создайте собственный класс - исключение, обрабатывающий ситуацию деления
# # на ноль.Проверьте его работу на данных, вводимых пользователем.При
# # вводе нуля в качестве делителя программа должна корректно
# # обработать эту ситуацию и не завершиться с ошибкой.
class DivisionError(Exception):
    def __init__(self,txt):
        self.txt=txt

try:
    divisible=float(input('Введите делимое: '))
    divider=float(input('Введите делитель: '))
    if divider==0:
        raise DivisionError("Делить на ноль нельзя")
except ValueError:
    print("Вы ввели не число")
except DivisionError as err:
    print(err)
else:
    division_result = divisible / divider
    print(f"Результат деления :{division_result}")
