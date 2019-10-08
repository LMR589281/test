import pygame
import time
pygame.init()
main_window = pygame.display.set_mode((800, 600))

def set_pixel(surf, x_pos, y_pos, colour):
    px_array=pygame.PixelArray(surf)
    px_array[x_pos-1:x_pos+1, y_pos-1:y_pos+1] = colour
    # time.sleep(5)
    #del px_array

def less_red():
    pixelMatrix=getPixels(pict)
    for pixel in pixelMatrix:
        value=getRed(pixel)
        setRedPixel(pixel, value*0.5)

running = True
while running:
    my_surface = pygame.Surface((200, 200))
    my_surface.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        main_window.fill((255, 255, 255))
        main_window.blit(my_surface, (0, 0))
        set_pixel(my_surface, 100, 100, (0,0,0))
        image = pygame.image.load('test.png')
        main_window.blit(image, (200,200))
        pygame.display.update()

pygame.quit()