import pygame
import sys
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

hand = pygame.image.load("images/mickey_hand.png")
center = (300, 300)

def draw_hand(angle):
    rotated = pygame.transform.rotate(hand, -angle)
    rect = rotated.get_rect(center=center)
    screen.blit(rotated, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    now = datetime.now()
    sec = now.second
    minute = now.minute

    sec_angle = sec * 6
    min_angle = minute * 6

    draw_hand(sec_angle)
    draw_hand(min_angle)

    pygame.display.flip()
    clock.tick(1)