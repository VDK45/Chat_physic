import pymunk as pm
import pygame as pg


class Doo(pm.Poly):
    '''
    Класс, описывающий ОБЩИЕ черты двух типов Ду (свободных и фиксированных).
    Этот класс модифицирует исходный класс pm.Poly. Мы не создаем класс с нуля, чтобы в дальнейшем использовать возможности
    обработки столкновений. МЫ НЕ БУДЕМ СОЗДАВАТЬ ЭКЗЕМПЛЯРЫ ЭТОГО КЛАССА. Класс Poly является модификацией класса Shape.'''

    def __init__(self, x, y, mass=100, moment=10000, r=100, h=10):
        # Вызываем метод __init__() класса pm.Poly (подробнее см. класс World).
        # Объекты класса Shape привязываются к объектам класса Body. Создаем такой объект на лету (pm.Body()).
        # [(-r,-h), (r,-h), (r,h), (-r,h)] -- координаты вершин многоугольника относительно объекта Body (~ центр масс тела).
        super().__init__(pm.Body(mass, moment), [(-r, -h), (r, -h), (r, h), (-r, h)])
        self.body.position = x, y
        self.rad = r
        # Логическая переменная: находится ли Ду на полу.
        self.ground = False

    def check_ground(self, world):
        '''
        Функция для проверки того,коснулся ли Ду пола.'''
        # Ду должен находиться от пола не дальше, чем на свой радиус.
        if self.body.position.y >= (world.ground_y - self.rad):
            self.ground = True
        else:
            self.ground = False


class DooFree(Doo):
    '''
    Класс, описывающий свойства и поведение свободных Ду.
    Модифицируем класс Doo.'''

    def __init__(self, x, y):
        # Переопределяем значение атрибутов
        # friction -- коэффициент трения
        # elasticity -- эластичность
        # collision_type -- очень важный параметр, позволит нам различать разные типы объектов,
        # а также обрабатывать их столкновения. Значение 0 будет соответствовать свободным Ду.
        super().__init__(x, y)
        # Переопределм значения атрибутов
        self.friction = 10
        self.elasticity = 0.5
        self.collision_type = 0
