# Начните работу над проектом «Склад оргтехники».Создайте класс, описывающий склад.А также
# класс «Оргтехника», который будет базовым для классов - наследников.Эти классы — конкретные
# типы оргтехники(принтер, сканер, ксерокс).В базовом классе определите параметры, общие
# для приведённых типов.В классах - наследниках реализуйте параметры, уникальные для каждого
# типа оргтехники
from collections import Counter
from itertools import count


# функция-декоратор,которая шифруется под вызываемую функцию,обратить внимание:
# функция принимает на борт 4!!! аргумента а не 3 как может показаться на первый взгляд,
# первый аргумент это экземпляр класса!!!
def our_decorator(function):
    def our_wapper(*args):
        my_list_wapper = list(args)
        if len(args) != 4:
            print('вы не верно ввели описание объекта')
        elif args[1].isalpha() and args[2].isdigit() and args[3].isdigit():
            resalt = function(*args)
            return resalt
        else:
            print('Вы не корректно ввели данные')

    return our_wapper


class TechnologyWarehouse:

    def __init__(self):
        self.name = (input('Наименование оргтехники: ')).lower()
        if self.name in ['ксерокс', 'сканер', 'принтер']:
            self.item_weight = input('Серийный номер экземпляра: ')
            self.unt_code = input('Код подразделения ,для которого преднозначен товар: ')
            self.my_tuple = tuple([self.name, self.item_weight, self.unt_code])
        else:
            print('данный товар не является нужной нам оргтехникой ')

    def __del__(self):
        pass

    def __str__(self):
        if self.name.lower() in ['ксерокс', 'сканер', 'принтер']:
            return f'Описание образца оргтехники:{self.my_tuple} '
        else:
            return f'Товар{self.name} без атрибутов'


# A = TechnologyWarehouse()#Принтер
# B = TechnologyWarehouse()#Сканер
# C = TechnologyWarehouse()#Ксерокс

my_list = []
# print(my_list[0])
for mn in count(1, 1):
    my_word = input('Хотите создать экземпляр класса оргтехника(нажмите Enter или наберите нет): ')
    if my_word.lower() == 'нет':
        break
    else:
        A = TechnologyWarehouse()
        if A.name not in ['ксерокс', 'сканер', 'принтер']:
            del A
        else:
            my_list.append(A)
# Необходимо ввести минимум два экземпляра класса
print(my_list)
print(my_list[0])
print(my_list[1])


class Stock():
    my_list_new = list()

    # Функция-конструктор выполняет функцию приёма товара на склад и формирует базу данных склада
    def __init__(self, subjects):
        for self.subject in subjects:
            if isinstance(self.subject, TechnologyWarehouse):  # принадлежит ли объект классу?
                self.my_list_new.append(self.subject.my_tuple)  # Список товаров для склада в виде списка кортежей
        self.name_dict = dict(
            Counter([lm[0] for lm in self.my_list_new]))  # Словарь товаров для склада(в функцию Counter
        # передаётся генератор списка имён.

    def __str__(self):
        return f'{self.name_dict}'

    # функция отгрузки товара сосклада.
    @our_decorator
    def goods_shipment(self, name, cod, item_weight):
        self.new_name = name.lower()
        if (self.new_name, cod, item_weight) not in self.my_list_new:
            print('такого товара на складе нет')
        else:
            print('Данный товар будет отгружен')
            self.name_dict[self.new_name] = self.name_dict[
                                                self.new_name] - 1  # уменьшает на еденицу товар с именем name
            self.my_list_new.remove((self.new_name, cod, item_weight))  # удаляет из списка кортежей искомый кортеж

    # функция приёма товара на склад
    @our_decorator
    def receipt_of_goods(self, name, cod, item_weight):
        self.new_name = name.lower()
        if (self.new_name, cod, item_weight) not in self.my_list_new:
            print('товар будет добавлен на склад')
            if self.new_name not in self.name_dict:
                self.name_dict[self.new_name] = 0
            self.name_dict[self.new_name] = self.name_dict[self.new_name] + 1
            self.my_list_new.append((name, cod, item_weight))
        else:
            print('данный товар уже на складе')


# проверка работы методов класса
C = Stock(my_list)
print(C.my_list_new)
print(C)
C.receipt_of_goods('сканер', '234', '432')
C.goods_shipment('Ксерокс', '123', '321')
print(C.my_list_new)
print(C.name_dict)
