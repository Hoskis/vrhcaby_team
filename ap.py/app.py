import pygame

def pohyb(bile, cerne):
    vybrane = None
    kliknuti = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN and kliknuti == 0:
                pos = pygame.mouse.get_pos()
                for circle in bile + cerne:
                    if circle.collidepoint(pos):
                        vybrane = circle
                        kliknuti = 1
                        break

            elif event.type == pygame.MOUSEBUTTONDOWN and kliknuti != 0:
                if vybrane:
                    pos = pygame.mouse.get_pos()
                    vybrane.center = pos
                    vybrane = None
                    kliknuti = 0

        window.blit(pozadi, (0, 0))
        for circle in bile:
            pygame.draw.circle(window, (255, 255, 0), circle.center, 20)
        for circle in cerne:
            pygame.draw.circle(window, (0, 0, 0), circle.center, 20)
        pygame.display.flip()

pygame.init()
window = pygame.display.set_mode((800, 600))
pozadi = pygame.image.load("bg.png")
bile =[(690,50),(690,90),(110,50),(110,90),(110,130),(110,170),(110,210),(305,540),(305,500),(305,460),(440,540),(440,500),(440,460),(440,420),(440,380)]
cerne =[(690,540),(690,500),(110,540),(110,500),(110,460),(110,420),(110,380),(305,50),(305,90),(305,130),(440,50),(440,90),(440,130),(440,170),(440,210)]

bile_circles = [pygame.Rect(bod[0]-20, bod[1]-20, 40, 40) for bod in bile]
cerne_circles = [pygame.Rect(bod[0]-20, bod[1]-20, 40, 40) for bod in cerne]

window.blit(pozadi, (0, 0))
pygame.display.flip()

pohyb(bile_circles, cerne_circles)