# https://github.com/kadir014/pygame-video
# setup pyglet & the video

path = r"[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art).mp4"
import pygame
from pygamevideo import Video

size = (960, 720)
window = pygame.display.set_mode(size)

video = Video(path)
video.set_size(size)
# start video
video.play()

running = True
# main loop
while running:
    ...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw video to display surface
    # this function must be called every tick
    video.draw_to(window, (0, 0))

    # set window title to current duration of video as hour:minute:second
    t = video.current_time.format("%h:%m:%s")
    pygame.display.set_caption(t)
    pygame.display.flip()
