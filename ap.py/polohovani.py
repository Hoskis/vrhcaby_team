import sdilene_polozky
        #76-135 = 1
def shoda(poloha_x,poloha_y):
        if poloha_y < 300:
                if 85 <= poloha_x <= 135:
                        prvni = [109,55]
                        sdilene_polozky.databaze = sdilene_polozky.data1
                        #136-185 =2
                elif (poloha_x >= 136) and (poloha_x <= 185):
                        prvni = [159,55]
                        sdilene_polozky.databaze = sdilene_polozky.data2
                        #186-235 =3
                elif (poloha_x >= 186) and (poloha_x <= 235):
                        prvni = [209,55]
                        sdilene_polozky.databaze = sdilene_polozky.data3
                        #236-285 =4
                elif (poloha_x >= 236) and (poloha_x <= 285):
                        prvni = [259,55]
                        sdilene_polozky.databaze = sdilene_polozky.data4
                        #286-335 =5
                elif (poloha_x >= 286) and (poloha_x <=335):
                        prvni = [309,55]
                        sdilene_polozky.databaze = sdilene_polozky.data5
                        #336-383 =6
                elif (poloha_x >= 336) and (poloha_x <= 383):
                        prvni = [359,55]
                        sdilene_polozky.databaze = sdilene_polozky.data6
                        #417-467 =7
                elif (poloha_x >= 417) and (poloha_x <= 467):
                        prvni = [443,55]
                        sdilene_polozky.databaze = sdilene_polozky.data7
                        #468-517 =8
                elif (poloha_x >= 468) and (poloha_x <= 517):
                        prvni = [493,55]
                        sdilene_polozky.databaze = sdilene_polozky.data8
                        #518-567 =9
                elif (poloha_x >= 518) and (poloha_x <= 567):
                        prvni = [543,55]
                        sdilene_polozky.databaze = sdilene_polozky.data9
                        #568-617 =10
                elif (poloha_x >= 568) and (poloha_x <= 617):
                        prvni = [593,55]
                        sdilene_polozky.databaze = sdilene_polozky.data10
                        #618-667 =11
                elif (poloha_x >= 618) and (poloha_x <= 667):
                        prvni = [643,55]
                        sdilene_polozky.databaze = sdilene_polozky.data11
                        #668-717 =12
                elif (poloha_x >= 668) and (poloha_x <= 717):
                        prvni = [693,55]
                        sdilene_polozky.databaze = sdilene_polozky.data12
        else:
                if 85 <= poloha_x <= 135:
                        prvni = [109,550]
                        sdilene_polozky.databaze = sdilene_polozky.data1
                        #136-185 =2
                elif (poloha_x >= 136) and (poloha_x <= 185):
                        prvni = [159,550]
                        sdilene_polozky.databaze = sdilene_polozky.data2
                        #186-235 =3
                elif (poloha_x >= 186) and (poloha_x <= 235):
                        prvni = [209,550]
                        sdilene_polozky.databaze = sdilene_polozky.data3
                        #236-285 =4
                elif (poloha_x >= 236) and (poloha_x <= 285):
                        prvni = [259,550]
                        sdilene_polozky.databaze = sdilene_polozky.data4
                        #286-335 =5
                elif (poloha_x >= 286) and (poloha_x <=335):
                        prvni = [309,550]
                        sdilene_polozky.databaze = sdilene_polozky.data5
                        #336-383 =6
                elif (poloha_x >= 336) and (poloha_x <= 383):
                        prvni = [359,550]
                        sdilene_polozky.databaze = sdilene_polozky.data6
                        #417-467 =7
                elif (poloha_x >= 417) and (poloha_x <= 467):
                        prvni = [443,550]
                        sdilene_polozky.databaze = sdilene_polozky.data7
                        #468-517 =8
                elif (poloha_x >= 468) and (poloha_x <= 517):
                        prvni = [493,550]
                        sdilene_polozky.databaze = sdilene_polozky.data8
                        #518-567 =9
                elif (poloha_x >= 518) and (poloha_x <= 567):
                        prvni = [543,550]
                        sdilene_polozky.databaze = sdilene_polozky.data9
                        #568-617 =10
                elif (poloha_x >= 568) and (poloha_x <= 617):
                        prvni = [593,550]
                        sdilene_polozky.databaze = sdilene_polozky.data10
                        #618-667 =11
                elif (poloha_x >= 618) and (poloha_x <= 667):
                        prvni = [643,550]
                        sdilene_polozky.databaze = sdilene_polozky.data11
                        #668-717 =12
                elif (poloha_x >= 668) and (poloha_x <= 717):
                        prvni = [693,550]
                        sdilene_polozky.databaze = sdilene_polozky.data12
        return prvni

