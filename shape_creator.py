import pymunk as pm
import pygame as pg
# Импортируем класс DooFree из файла doo.py
from doo import DooFree


class ShapeCreator():
    '''
        Класс, содержащий методы для создания и удаления объектов разных типов.
    '''

    def __init__(self, world, space):
        # В качестве атрибутов задаем пространство симуляции и игровую область.
        self.world = world
        self.space = space

    def create_free_doo(self, x, y):
        '''
            Функция для создания свободного Ду.
        '''
        free_doo = DooFree(x, y)
        # В основе Ду лежит динамическое тело, поэтому
        # в пространство симуляции добавляем и тело, и его форму.
        self.space.add(free_doo.body, free_doo)
        # Добавляем нового Ду в массив free_do для дальнейшего использования
        self.world.free_doos.append(free_doo)

    def remove_escaped_doos(self):
        '''
        Функция для удаления Ду, вышедших за границы игровой области.
        '''
        for doo in self.world.free_doos:
            if doo.body.position.x < 0 or doo.body.position.x > self.world.width:
                # Необходимо удалить и тело (Body) и его форму. Автоматически форма не удалится.
                self.world.free_doos.remove(doo)
                self.space.remove(doo.body, doo)
            elif doo.body.position.y > self.world.height:
                self.world.free_doos.remove(doo)
                self.space.remove(doo.body, doo)

    def draw_text(self, text, font, color, surface, x, y):
        pass
