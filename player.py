from circleshape import *
from constants import *
from shot import *
import pygame

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        # Create a surface for the sprite
        self.image = pygame.Surface((PLAYER_RADIUS*2, PLAYER_RADIUS*2), pygame.SRCALPHA)
        # Create a rect for positioning
        self.rect = self.image.get_rect(center=(x, y))
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
            # Update the cooldown timer
        if self.shot_timer > 0:
            self.shot_timer -= dt
        # Ensure timer doesn't go below 0
            if self.shot_timer < 0:
                self.shot_timer = 0
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_timer == 0:
                self.shoot()
                self.shot_timer = PLAYER_SHOT_COOLDOWN


    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # Update the rect to match the new position
        self.rect.center = self.position
    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        new_shot.velocity *= PLAYER_SHOOT_SPEED