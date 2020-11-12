import pygame
import random


pygame.init()

FONT = pygame.font.Font("freesansbold.ttf", 25)
BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_BLUE = (0, 98, 102)
DARK_BLUE2 = (18, 137, 167)
MID_GREEN = (0, 148, 50)
LIGHT_GREEN = (0, 148, 50)
LIGHT_GREEN2 = (0, 148, 50)


class MouseSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.mouseDown = False
        self.prevMouseDown = False
        self.activate = False
        self.update(x, y)

    def update(self, x, y):
        self.mx = x
        self.my = y
        self.rect = pygame.Rect(self.mx, self.my, 1, 1)

    def mouse_down(self):
        self.mouseDown = True

    def mouse_up(self):
        self.mouseDown = False

    def detect_collision(self, current_state, sprites):
        sprite_collision_list = pygame.sprite.spritecollide(self, sprites, False)
        if len(sprite_collision_list) > 0:
            sprite_collision = sprite_collision_list[-1]
            if self.mouseDown and not self.prevMouseDown:
                sprite_collision.click_down()
                self.activate = True
            elif self.prevMouseDown and not self.mouseDown and self.activate:
                self.activate = False
                sprite_collision.click_up(current_state)

        if self.mouseDown:
            self.prevMouseDown = True
        else:
            self.prevMouseDown = False


class ButtonSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, state, baseColor, clickColor, textColor=(255,255,255), text=""):
        super().__init__()
        self.state = state
        self.baseColor = baseColor
        self.clickColor = clickColor
        self.text = text
        self.font = FONT

        self.isClicked = False
        self.color = baseColor
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.update()

    def update(self):
        if self.isClicked:
            self.color = self.clickColor
        else:
            self.color = self.baseColor
        self.image.fill(self.color)
        textImage = self.font.render(self.text, True, WHITE)
        textRect = textImage.get_rect(center=(self.image.get_width()//2, self.image.get_height()//2))
        self.image.blit(textImage, textRect)

    def click_down(self):
        self.isClicked = True

    def click_up(self, state):
        self.isClicked = False
        state.done = True
        state.nextState = self.state

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class TextboxSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, baseColor, textColor=(255,255,255), text=""):
        super().__init__()
        self.baseColor = baseColor
        self.textColor = textColor
        self.text = text
        self.font = FONT

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image.fill(self.baseColor)
        textImage = self.font.render(self.text, True, WHITE)
        textRect = textImage.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
        self.image.blit(textImage, textRect)

    def click_down(self, state=False):
        pass

    def click_up(self, state=False):
        pass

class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wins = 0
        self.losses = 0
        self.opponent = False
        self.lastOpponent


