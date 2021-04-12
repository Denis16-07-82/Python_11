# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNumbers:
    def __init__(self, Renumbers, Imnumbers):
        self.Renumbers = Renumbers
        self.Imnumbers = Imnumbers

    def __str__(self):
        return f'Наше комплексное число:{self.Renumbers}+{self.Imnumbers}*j'

    def __add__(self, other):
        return ComplexNumbers(self.Renumbers + other.Renumbers, self.Imnumbers + other.Imnumbers)

    def __sub__(self, other):
        return ComplexNumbers(self.Renumbers - other.Renumbers, self.Imnumbers - other.Imnumbers)

    def __mul__(self, other):
        return ComplexNumbers(self.Renumbers * other.Renumbers - self.Imnumbers * other.Imnumbers,
                              self.Renumbers * other.Imnumbers + self.Imnumbers * other.Renumbers)

    def __truediv__(self, other):
        return ComplexNumbers((self.Renumbers * other.Renumbers + self.Imnumbers * other.Imnumbers) / (
                    other.Renumbers ** 2 + other.Imnumbers ** 2),
                              (other.Renumbers * self.Imnumbers - self.Renumbers * other.Imnumbers) / (
                                          other.Renumbers ** 2 + other.Imnumbers ** 2))


z_1=ComplexNumbers(5,6)
z_2=ComplexNumbers(7,3)
z_3=ComplexNumbers(1,2)
print(z_1+z_2+z_3)
print((z_1-z_2)*z_3)
print(z_1*z_2)
print(z_1/z_2)
