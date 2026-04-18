import pygame
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

tracks = [
    "music/sample_tracks/track1.wav",
    "music/sample_tracks/track2.wav"
]

current = 0

def play():
    pygame.mixer.music.load(tracks[current])
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global current
    current = (current + 1) % len(tracks)
    play()

def prev_track():
    global current
    current = (current - 1) % len(tracks)
    play()

font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    screen.fill((255, 255, 255))

    text = font.render(f"Track: {tracks[current].split('/')[-1]}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    pygame.display.flip()