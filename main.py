import pygame
import time
import random
from rule import *

global x, y, pos


class World:
    def __init__(self, width, height, wow, x1, y1):
        self.width = width
        self.height = height
        self.wow = wow
        self.x = x1
        self.y = y1

    def divide(self):
        global pos
        for i in range(0, self.width//self.wow):
            if i < x/self.wow < i + 1:
                self.x = i
        for j in range(0, self.height//self.wow):
            if j < y/self.wow < y + 1:
                self.y = j
        pos = self.x, self.y
        return pos


def draw(path, position):
    screen.blit(path, position)


def update():
    pygame.display.update()


def color(num):
    if num == 0:
        return black
    elif num == 1:
        return white


if __name__ == "__main__":
    pygame.init()
    World_width = 800
    World_height = 500
    Cell_size = 20
    rule = Rule(World_width, World_height, Cell_size, 0)
    world = World(World_width, World_height, Cell_size, 0, 0)
    # 创建铺满的细胞
    rule.run()
    size = rule.width, rule.height + 60
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game of Life")
    time_running = 0

    Black = pygame.color.Color("black")
    white = pygame.image.load("picture/white.png")
    white = pygame.transform.smoothscale(white, (rule.wow, rule.wow))
    black = pygame.image.load("picture/black.png")
    black = pygame.transform.smoothscale(black, (rule.wow, rule.wow))
    red = pygame.image.load("picture/red.png")
    red = pygame.transform.smoothscale(red, (rule.wow, rule.wow))
    green = pygame.image.load("picture/green.png")
    green = pygame.transform.smoothscale(green, (rule.wow, rule.wow))
    blue = pygame.image.load("picture/blue.png")
    blue = pygame.transform.smoothscale(blue, (World_width, 60))
    draw(blue, (0, World_height))
    txt_state_0 = pygame.font.Font("font/Arial.ttf", 20).render("Creating Mode(print R to run)", True, Black)
    txt_state_0_1 = pygame.font.Font("font/Arial.ttf", 20).render("Print Q to create randomly", True, Black)
    txt_state_1 = pygame.font.Font("font/Arial.ttf", 20).render("Running···(print SPACE to modify)", True, Black)

    while True:
        x, y = pygame.mouse.get_pos()
        for cell in cell_list:
            if cell.charge == 0:
                dest = (cell.position[0] * rule.wow, cell.position[1] * rule.wow)
                draw(color(cell.is_live), dest)
            cell.charge = 0
        if rule.state == 0:
            draw(blue, (0, World_height))
            draw(txt_state_0, ((World_width - txt_state_0.get_width())/2, World_height))
            draw(txt_state_0_1, ((World_width - txt_state_0_1.get_width())/2, World_height + 30))
        elif rule.state == 1:
            draw(blue, (0, World_height))
            draw(txt_state_1, ((World_width - txt_state_0.get_width())/2, World_height))
            txt_time = pygame.font.Font("font/Arial.ttf", 20).render("Time: " + str(time_running), True, Black)
            draw(txt_time, ((World_width - txt_time.get_width())/2, World_height + 30))
        update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and rule.state == 0:
                # 获取坐标pos = (x, y)
                world.divide()
                for cell in cell_list:
                    if cell.position == pos:
                        cell.convert()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rule.state = 1
                if event.key == pygame.K_SPACE:
                    rule.state = 0
                if event.key == pygame.K_q:
                    for cell in cell_list:
                        cell.is_live = random.randint(0, 1)

        if rule.state == 1:
            rule.get_neighbour()
            for cell in cell_list:
                cell.change()
            time_running = time_running + 1
            # time.sleep(1)
        if rule.state == 0:
            world.divide()
            for cell in cell_list:
                if cell.position == pos:
                    cell.charge = 1
                    dest = (cell.position[0] * rule.wow, cell.position[1] * rule.wow)
                    if cell.is_live == 0:
                        draw(green, dest)
                        update()
                    elif cell.is_live == 1:
                        draw(red, dest)
                        update()
