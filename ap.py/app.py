import pygame
import sdilene_polozky
import polohovani


def pohyb(bile, cerne):
    vybrane = None
    kliknuti = 0
    
    while True:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            #první kliknutí(výběr figurky)
            elif event.type == pygame.MOUSEBUTTONDOWN and kliknuti == 0:
                pos = pygame.mouse.get_pos()
                rada = polohovani.shoda(int(pos[0]),int(pos[1]))
                zaznam = sdilene_polozky.databaze
                for circle in bile + cerne:
                    if circle.collidepoint(zaznam[-1]):
                        vybrane = circle
                        kolecko = pos
                        kliknuti = 1
                        break
            #druhé kliknutí(přesun figurky)
            elif event.type == pygame.MOUSEBUTTONDOWN and kliknuti != 0:
                souradnice = pygame.mouse.get_pos()
                #funkce na určení nového pole
                print(zaznam)
                prvni = polohovani.shoda(int(souradnice[0]),int(souradnice[1]))
                databaze_zaznamu = sdilene_polozky.databaze
                print(databaze_zaznamu)
                if vybrane:
                    pos = prvni
                    while pos in sdilene_polozky.databaze:
                        if rada == pos:
                            pos = None
                            kliknuti = 0
                            break
                        else:
                            poradi = len(sdilene_polozky.databaze)-1
                            if pos[1] < 300:
                                prvni[1]+= poradi*40
                            else:
                                prvni[1]-= poradi*40    
                            pos = prvni
                            if pos in sdilene_polozky.databaze:
                                break
                    if pos != None:
                        zaznam.pop(-1)
                        sdilene_polozky.databaze.append(pos)
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
hodnota = [0,0]
pozadi = pygame.image.load("bg.png")
bile =[(690,50),(690,90),(110,50),(110,90),(110,130),(110,170),(110,210),(305,540),(305,500),(305,460),(440,540),(440,500),(440,460),(440,420),(440,380)]
cerne =[(690,540),(690,500),(110,540),(110,500),(110,460),(110,420),(110,380),(305,50),(305,90),(305,130),(440,50),(440,90),(440,130),(440,170),(440,210)]
pozadovane = [[]]
bile_circles = [pygame.Rect(bod[0]-15, bod[1]-15, 40, 40) for bod in bile]
cerne_circles = [pygame.Rect(bod[0]-15, bod[1]-15, 40, 40) for bod in cerne]
window.blit(pozadi, (0, 0))
pygame.display.flip()

pohyb(bile_circles, cerne_circles)