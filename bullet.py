import pygame


class Bullet(pygame.sprite.Sprite):
    missed_count = 0

    def __init__(self, pos, screen_width) -> None:
        super().__init__()

        # set bullet width and height
        bullet_width = 20
        bullet_height = 4

        self.image = pygame.Surface((bullet_width, bullet_height))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.bullet_speed = -10
        self.width_x_constraint = screen_width
        self.offset_x = 50

    def destroy(self):
        if(self.rect.x <= -self.offset_x or self.rect.x >= (self.width_x_constraint + self.offset_x)):
            self.kill()
            Bullet.missed_count = Bullet.missed_count + 1
            print(Bullet.missed_count)

    def update(self):
        self.rect.x += self.bullet_speed
        self.destroy()
