import pygame

window = pygame.display.set_mode((800,600))
pozadi = pygame.image.load("bg.png")
body = []

class Okno:
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                body.append(pygame.mouse.get_pos())              
        for bod in body:
            
            window.blit(pozadi, (0, 0))
            pygame.draw.circle(window, (0, 0, 0), (bod), 20)
            pygame.display.flip()
Okno