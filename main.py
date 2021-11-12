import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False  # Интеграция Pygame + Pymunk
# Ширина высота
RES = WIDTH, HEIGHT = 1280, 720
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

# Опция отрисовка физ-оъбектов
draw_options = pymunk.pygame_util.DrawOptions(surface)

# Гравитация по y
space = pymunk.Space()
space.gravity = 0, 4000


def create_ball(space):
    ball_mass, ball_radius = 1, 25
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = randrange(30, WIDTH), randrange(10, 200)
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8  # Упругость
    ball_shape.friction = 0.5  # Кручение
    space.add(ball_body, ball_shape)


def create_box(space):
    box_mass, box_size = 1, (300, 30)
    box_moment = pymunk.moment_for_box(box_mass, box_size)
    box_body = pymunk.Body(box_mass, box_moment)
    box_body.position = randrange(30, WIDTH), randrange(10, 200)
    box_shape = pymunk.Poly.create_box(box_body, box_size)
    box_shape.elasticity = 0.8
    box_shape.friction = 1
    box_shape.color = [randrange(256), randrange(150), randrange(256), randrange(200, 256)]  # Red, Green, Blue, ???
    space.add(box_body, box_shape)


# Платформа
segment_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
segment_shape.elasticity = 1
space.add(segment_shape)


while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                # create_ball(space)
                create_box(space)


    # Единица времени pymunk
    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)
