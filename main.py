import pygame  # pygame version 2.1.2
import sys
from balloon import Balloon
from bullet import Bullet
from player import Player

# SCREEN ------------------------------------
# declare screen properties
screen_width = 800
screen_height = 500
frame_rate = 60

# BACKGROUND -----------------------------------------
background_color = (30, 30, 30)

# GAME -----------------------------------------------


class Game:
    def __init__(self) -> None:
        # Player Setup
        player_sprite = Player(
            ((screen_width / 1.1), screen_height/2), screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Balloon setup
        # balloon speed is 10 times slower than the speed of the bullets
        self.balloon_speed = 1
        balloon_sprite = Balloon(
            self.balloon_speed, (0 + 40), screen_height/2, screen_height)
        self.balloon = pygame.sprite.GroupSingle(balloon_sprite)

        # Game setup
        self.gameOver = False
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)

    def display_missed_count(self):
        missed_count_text = self.font.render(
            f'Game Over! Missed Shot: {Bullet.missed_count}', False, 'white')
        missed_count_rect = missed_count_text.get_rect(
            midbottom=(screen_width / 2, screen_height/2))
        screen.blit(missed_count_text, missed_count_rect)

    def run(self):
        # draw all sprite groups
        self.player.sprite.bullets.draw(screen)
        self.player.draw(screen)
        self.balloon.draw(screen)
        if self.gameOver:
            self.display_missed_count()

        # update all sprite groups
        if not self.gameOver:
            self.player.update()
            self.balloon.update()
            self.collision_checker()

    def collision_checker(self):
        # check for any collision between balloon and bullet
        if self.player.sprite.bullets:
            for bullet in self.player.sprite.bullets:
                if pygame.sprite.spritecollide(bullet, self.balloon, True):
                    bullet.kill()
                    self.gameOver = True


# WINDOW ---------------------------------------------
# initialize the window here
if __name__ == "__main__":  # to make sure that we are running on the main file
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(background_color)
        game.run()  # run the game here
        pygame.display.flip()
        clock.tick(frame_rate)
