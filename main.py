# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import *
from circleshape import *
from constants import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()
    Shot.containers = (updatable, all_shots, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #print(pygame.get_init())
        screen.fill("black")
        updatable.update(dt)
        for single_asteroid in asteroids:
            for single_shot in all_shots:
                if single_asteroid.collision(single_shot):
                    single_shot.kill()
                    single_asteroid.kill()
            if single_asteroid.collision(player):
                print("Game over!")
                sys.exit()

        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print (clock.get_fps())
    
    

if __name__ == "__main__":
        main()