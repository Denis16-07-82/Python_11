# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re


class Data:
    RE_NAME = re.compile(r'^(\d{2})\-(\d{1,2})\-(\d{4})$')

    def __init__(self, my_str):
        if self.RE_NAME.findall(my_str):
            self.my_str = self.RE_NAME.findall(my_str)[0]
        else:
            self.my_str = my_str

    @classmethod
    def data_method(cls, my_str):
        try:
            print(
                f'число: {int(Data(my_str).my_str[0])} месяц: {int(Data(my_str).my_str[1])} год: {int(Data(my_str).my_str[2])}')
        except ValueError:
            print('не верный формат')

    @staticmethod
    def data_check(my_str):
        try:
            if 0 <= int(Data(my_str).my_str[0]) < 31 and 1 <= int(Data(my_str).my_str[1]) < 12 and 0 <= int(
                    Data(my_str).my_str[2]):
                print(f'Формат сооветствует формату «день-месяц-год» ')

            else:
                print('Даты не входят в диапазон- число:от 0 до 31,месяц:от 1 до 12,год:от 0 и больше ')
        except ValueError:
            print('не верный формат')


A = Data('12-03-2021')
print(A.my_str)
Data.data_method('12-03-2021')
Data.data_check('12-03-2021')
