import pygame
from bullet import Bullet
# player class has to inherit from Sprite class in order to inherit the behaviours


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, constraint) -> None:
        super().__init__()
        self.image = pygame.image.load(
            'graphics/cannon.jpg').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 5  # declare the speed of the player

        # to prevent the player from moving out of the screen upper and lower boundaries
        self.max_y_constraint = constraint

        # to set the timer for shooting
        self.shoot_ready = True
        self.shoot_timer = 0
        self.shoot_cooldown = 600  # milliseconds

        # to create bullets
        self.bullets = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if keys[pygame.K_SPACE] and self.shoot_ready:
            self.shoot()
            # this force the player to wait for a period of time before shooting again
            self.shoot_ready = False
            self.shoot_timer = pygame.time.get_ticks()

    def recharge(self):
        if not self.shoot_ready:
            current_time = pygame.time.get_ticks()
            if (current_time - self.shoot_timer) >= self.shoot_cooldown:
                self.shoot_ready = True

    def constraint(self):
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= (self.max_y_constraint - self.rect.height):
            self.rect.y = (self.max_y_constraint - self.rect.height)

    def shoot(self):
        print("Shoot")
        self.bullets.add(Bullet(self.rect.center, self.rect.right))

    def update(self) -> None:
        self.get_input()
        self.constraint()
        self.recharge()
        self.bullets.update()
