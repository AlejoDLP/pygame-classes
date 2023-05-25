import pygame
import sys
import button


SCREENWIDTH, SCREENHEIGHT = 1920, 1080
FPS = 60
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

class Game:
    def __init__(self) :
        pygame.init()
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('level')
        self.start = Start(screen, self.gameStateManager)
        self.level = Level(screen, self.gameStateManager)

        self.states = {'start': self.start, 'level': self.level}
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)



class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('blue')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.gameStateManager.set_state('start')

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('red')

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()
