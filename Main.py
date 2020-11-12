import pygame
import sys

import Sprites as sp

BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_BLUE = (0, 98, 102)
DARK_BLUE2 = (18, 137, 167)
MID_GREEN = (0, 148, 50)
LIGHT_GREEN = (0, 148, 50)
LIGHT_GREEN2 = (0, 148, 50)
GRAY_GREEN = (170, 189, 170)

class Scene:
    def __init__(self, screen, states, start_state):
        self.running = True
        self.screen = screen
        self.states = states
        self.clock = pygame.time.Clock()
        self.state = states[start_state]

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.event_handler()
            self.update()

    def event_handler(self):
        mx, my = pygame.mouse.get_pos()
        mouse.update(mx, my)
        for event in pygame.event.get():
            self.state.event_handler(event)

    def update(self):
        self.state.update()
        if self.state.done:
            self.change_state()

    def change_state(self):
        if self.state.nextState == "QUIT":
            self.running = False
        elif self.state.nextState == "BACK":
            self.state.done = False
            self.state = self.last_state
        else:
            self.last_state = self.state
            nextState = self.state.nextState
            self.state.done = False
            self.state = self.states[nextState]


class GameState:
    def __init__(self):
        self.quit = False
        self.done = False
        self.nextState = False
        self.gameLogic = GameLogic()

    def update(self):
        pass

    def event_handler(self, event):
        pass


class Main(GameState):
    def __init__(self):
        super().__init__()
        self.allSprites = pygame.sprite.Group(
            sp.TextboxSprite(360, 90, 180, 420, GRAY_GREEN),
            sp.TextboxSprite(370, 100, 160, 50, LIGHT_GREEN2, text="Main Menu"),
            sp.ButtonSprite(400, 300, 100, 50, "GAME", LIGHT_GREEN, DARK_BLUE, textColor=DARK_BLUE2, text="Play"),
            sp.ButtonSprite(400, 400, 100, 50, "CONFIRM", LIGHT_GREEN, DARK_BLUE, textColor=DARK_BLUE2, text="Quit")
            )

    def update(self):
        mouse.detect_collision(self, self.allSprites)
        screen.fill((230,250,200))
        redraw_screen(self.allSprites)

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.nextState = "CONFIRM"
            self.done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse.mouse_down()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse.mouse_up()

class GameSetup(GameState):
    
class Game(GameState):
    def __init__(self):
        super().__init__()
        self.allSprites = pygame.sprite.Group(
            sp.ButtonSprite(50, 50, 100, 50, "MAINMENU", pygame.Color('steelblue1'), BLACK, text="Back")
            )
        for ()
        self.allSprites.add()


    def update(self):
        mouse.detect_collision(self, self.allSprites)

        screen.fill((230, 250, 200))
        redraw_screen(self.allSprites)

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.nextState = "CONFIRM"
            self.done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse.mouse_down()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse.mouse_up()


class Confirm(GameState):
    def __init__(self):
        super().__init__()
        self.allSprites = pygame.sprite.Group(
            sp.ButtonSprite(390, 450, 50, 50, "QUIT", pygame.Color('steelblue1'), BLACK, text="yes"),
            sp.ButtonSprite(460, 450, 50, 50, "BACK", pygame.Color('steelblue1'), BLACK, text="no")
            )

    def update(self):
        mouse.detect_collision(self, self.allSprites)
        screen.fill((230, 250, 200))
        redraw_screen(self.allSprites)

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
            self.done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse.mouse_down()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse.mouse_up()


class GameLogic:
    def __init__(self):
        super().__init__()
        all_sprites
def redraw_screen(sprites):
    sprites.update()
    sprites.draw(screen)
    pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    FONT = pygame.font.Font("freesansbold.ttf", 25)

    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("simulation!")
    states = {"MAINMENU": Main(),
              "GAME": Game(),
              "CONFIRM": Confirm(),
              }
    mouse = sp.MouseSprite(0,0)
    scene = Scene(screen, states, "MAINMENU")
    scene.run()
    pygame.quit()
    sys.exit()