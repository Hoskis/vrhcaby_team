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
                x = 0
                pos = pygame.mouse.get_pos()
                rada = polohovani.shoda(int(pos[0]),int(pos[1]))
                zaznam = sdilene_polozky.databaze
                prv_vyb = zaznam[-1]
                print(zaznam[-1])               
                
                for policko in sdilene_polozky.bile:
                    if policko == prv_vyb:
                        print(sdilene_polozky.bile)
                        poradi_vrch = x
                        print(poradi_vrch)
                        break
                    x += 1
                x = 0

                for policko in sdilene_polozky.cerne:
                    if policko == prv_vyb:
                        print(sdilene_polozky.cerne)
                        poradi_vrch = x
                        print(poradi_vrch)
                        break
                    x += 1
                
                for circle in bile:
                    if circle.collidepoint(zaznam[-1]):
                        barva = 1
                        vybrane = circle
                        kolecko = pos
                        kliknuti = 1
                        break
                      
                for circle in cerne:
                    if circle.collidepoint(zaznam[-1]):
                        barva = 2
                        vybrane = circle
                        kolecko = pos
                        kliknuti = 1
                        break

            #druhé kliknutí(přesun figurky)
            elif event.type == pygame.MOUSEBUTTONDOWN and kliknuti != 0:
                souradnice = pygame.mouse.get_pos()
                #funkce na určení nového pole
                prvni = polohovani.shoda(int(souradnice[0]),int(souradnice[1]))
                if prvni in sdilene_polozky.bile:
                    barva_v = 1
                elif prvni in sdilene_polozky.cerne:
                    barva_v = 2
                else:
                    barva_v = barva
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
                            pos = [int(prvni[0]),int(prvni[1])]
                            if pos in sdilene_polozky.databaze:
                                break
                    if pos != None and barva == barva_v:
                        zaznam.pop(-1)
                        sdilene_polozky.databaze.append(pos)
                        vybrane.center = pos
                        if barva == 1:
                            sdilene_polozky.bile.pop(poradi_vrch)
                            sdilene_polozky.bile.append(pos)
                        if barva == 2:
                            sdilene_polozky.cerne.pop(poradi_vrch)
                            sdilene_polozky.cerne.append(pos)
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
pozadovane = [[]]
bile_circles = [pygame.Rect(bod[0]-15, bod[1]-15, 40, 40) for bod in sdilene_polozky.bile]
cerne_circles = [pygame.Rect(bod[0]-15, bod[1]-15, 40, 40) for bod in sdilene_polozky.cerne]
window.blit(pozadi, (0, 0))
pygame.display.flip()

pohyb(bile_circles, cerne_circles)