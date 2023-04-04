import pygame

window = pygame.display.set_mode((800,600))
pozadi = pygame.image.load("bg.png")
bile = [(690,50),(690,90),(110,50),(110,90),(110,130),(110,170),(110,210),(305,540),(305,500),(305,460),(440,540),(440,500),(440,460),(440,420),(440,380)]
cerne = [(690,540),(690,500),(110,540),(110,500),(110,460),(110,420),(110,380),(305,50),(305,90),(305,130),(440,50),(440,90),(440,130),(440,170),(440,210)]
window.blit(pozadi, (0, 0))

class Okno:
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        for bod in bile:
           pygame.draw.circle(window, (255, 255, 0), (bod), 20)
        for bod in cerne:
           pygame.draw.circle(window, (0, 0, 0), (bod), 20)
            
        pygame.display.flip()
Okno