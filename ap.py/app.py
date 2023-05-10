import pygame
import sdilene_polozky
import polohovani

bile_circles = [pygame.Rect(bod[0]-15, bod[1]-15, 40, 40) for bod in sdilene_polozky.bile]
cerne_circles = [pygame.Rect(bod[0]-15, bod[1]-15, 40, 40) for bod in sdilene_polozky.cerne]
window = pygame.display.set_mode((800, 600))
pozadi = pygame.image.load("bg.png")



def pohyb(bile, cerne):
    #vybrane = které kolečko se přesouvá
    vybrane = None
    #kliknuti(0)=vyběr;kliknuti(1)=přesun
    kliknuti = 0        
    # hrac 0 = bily / hrac 1 = cerny
    hrac = 0
    # pocet tahu hrace
    tah = 0
    # max pocet zahrani
    max_tahu = 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            #první kliknutí(výběr figurky)
            elif event.type == pygame.MOUSEBUTTONDOWN and kliknuti == 0:
                poradi_seznamu = 0
                prvni_vyber = pygame.mouse.get_pos()
                #urceni rady
                rada = polohovani.shoda(int(prvni_vyber[0]),int(prvni_vyber[1]))
                zaznam = sdilene_polozky.databaze
                prv_vyb = zaznam[-1]            
                
                for policko in sdilene_polozky.bile:
                    if policko == prv_vyb:
                        poradi_vrch = poradi_seznamu
                        break
                    poradi_seznamu += 1
                poradi_seznamu = 0

                for policko in sdilene_polozky.cerne:
                    if policko == prv_vyb:
                        poradi_vrch = poradi_seznamu
                        break
                    poradi_seznamu += 1
                #vystupni data: rada = první prvek ve vybrané řadě; zaznam = seznam vsech figurek; poradi_vrch = na které pozici v seznamu všech figurek je vybraná figurka(pro přesun na jinou pozici)
                #-----------------------------poradi hracu podle barvy (zalezi jestli hrac je bily nebo cerny a jestli je vybrana figurka jeho)--------------------------------
                if hrac == 0 and prv_vyb in sdilene_polozky.bile:
                    for circle in bile:
                        if circle.collidepoint(zaznam[-1]):
                            barva = 1
                            vybrane = circle
                            kliknuti = 1
                            break
                elif hrac == 1 and prv_vyb in sdilene_polozky.cerne: 
                    for circle in cerne: 
                        if circle.collidepoint(zaznam[-1]):
                            barva = 2
                            vybrane = circle
                            kliknuti = 1
                            break
                else:
                    kliknuti = 0
                    break
                #Vystupni data: barva = cerna(2) nebo bila(1) figurka pro pohyb; vybrane = kolečko na které se poprvé kliklo a bude se presouvat; kliknutí = stav vyběr/přesun
                
            #druhé kliknutí(přesun figurky)
            elif event.type == pygame.MOUSEBUTTONDOWN and kliknuti != 0:
                souradnice = pygame.mouse.get_pos()
                #určení nově vybrané řady
                prvni = polohovani.shoda(int(souradnice[0]),int(souradnice[1]))
                
                #____urcení barvy vybraného pole_____
                if prvni in sdilene_polozky.bile:
                    barva_v = 1
                elif prvni in sdilene_polozky.cerne:
                    barva_v = 2
                else:
                    barva_v = barva
                #____________________________________
                
                if vybrane:
                    pos = prvni
                    while pos in sdilene_polozky.databaze:
                        # když je první a druhá vybraná řada stejná (nic se nestane)
                        if rada == pos:
                            pos = None
                            kliknuti = 0
                            break
                        #__rozhodne jestli je řada dole nebo nahoře a určí na jakém místě bude nová figurka__
                        else:
                            poradi = len(sdilene_polozky.databaze)-1
                            if pos[1] < 300:
                                prvni[1]+= poradi*40
                            else:
                                prvni[1]-= poradi*40    
                            pos = [int(prvni[0]),int(prvni[1])]
                            if pos in sdilene_polozky.databaze:
                                break
                    
                    # finalní kontrola jestli jsou figurky stejné barvy a je dostupná nová pozice a následný zápis do listů 
                    if pos != None and barva == barva_v:
                        zaznam.pop(-1)
                        sdilene_polozky.databaze.append(pos)
                        vybrane.center = pos
                        if barva == 1:
                            sdilene_polozky.bile.pop(poradi_vrch)
                            sdilene_polozky.bile.append(pos)
                            tah += 1
                            if tah >= max_tahu:
                                hrac = 1
                                tah = 0
                        if barva == 2:
                            sdilene_polozky.cerne.pop(poradi_vrch)
                            sdilene_polozky.cerne.append(pos)
                            tah += 1
                            if tah >= max_tahu:
                                hrac = 0
                                tah = 0
                    # resetování proměnných
                    vybrane = None
                    kliknuti = 0
                
        # vykreslování figurek na hrací plochu + pozadí
        window.blit(pozadi, (0, 0))
        for circle in bile:
            pygame.draw.circle(window, (255, 255, 0), circle.center, 20)
        for circle in cerne:
            pygame.draw.circle(window, (0, 0, 0), circle.center, 20)
        pygame.display.flip()
    
pohyb(bile_circles, cerne_circles)

