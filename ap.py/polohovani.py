import sdilene_polozky
        #76-135 = 1
def shoda(poloha_x,poloha_y):
        if poloha_y < 300:
                if 85 <= poloha_x <= 135:
                        prvni = [109,50]
                        sdilene_polozky.databaze = sdilene_polozky.data13
                        #136-185 =2
                elif (poloha_x >= 136) and (poloha_x <= 185):
                        prvni = [159,50]
                        sdilene_polozky.databaze = sdilene_polozky.data14
                        #186-235 =3
                elif (poloha_x >= 186) and (poloha_x <= 235):
                        prvni = [209,50]
                        sdilene_polozky.databaze = sdilene_polozky.data15
                        #236-285 =4
                elif (poloha_x >= 236) and (poloha_x <= 285):
                        prvni = [259,50]
                        sdilene_polozky.databaze = sdilene_polozky.data16
                        #286-335 =5
                elif (poloha_x >= 286) and (poloha_x <=335):
                        prvni = [309,50]
                        sdilene_polozky.databaze = sdilene_polozky.data17
                        #336-383 =6
                elif (poloha_x >= 336) and (poloha_x <= 383):
                        prvni = [359,50]
                        sdilene_polozky.databaze = sdilene_polozky.data18
                        #417-467 =7
                elif (poloha_x >= 417) and (poloha_x <= 467):
                        prvni = [443,50]
                        sdilene_polozky.databaze = sdilene_polozky.data19
                        #468-517 =8
                elif (poloha_x >= 468) and (poloha_x <= 517):
                        prvni = [493,50]
                        sdilene_polozky.databaze = sdilene_polozky.data20
                        #518-567 =9
                elif (poloha_x >= 518) and (poloha_x <= 567):
                        prvni = [543,50]
                        sdilene_polozky.databaze = sdilene_polozky.data21
                        #568-617 =10
                elif (poloha_x >= 568) and (poloha_x <= 617):
                        prvni = [593,50]
                        sdilene_polozky.databaze = sdilene_polozky.data22
                        #618-667 =11
                elif (poloha_x >= 618) and (poloha_x <= 667):
                        prvni = [643,50]
                        sdilene_polozky.databaze = sdilene_polozky.data23
                        #668-717 =12
                elif (poloha_x >= 668) and (poloha_x <= 717):
                        prvni = [693,50]
                        sdilene_polozky.databaze = sdilene_polozky.data24
        else:
                if 85 <= poloha_x <= 135:
                        prvni = [109,540]
                        sdilene_polozky.databaze = sdilene_polozky.data12
                        #136-185 =2
                elif (poloha_x >= 136) and (poloha_x <= 185):
                        prvni = [159,540]
                        sdilene_polozky.databaze = sdilene_polozky.data11
                        #186-235 =3
                elif (poloha_x >= 186) and (poloha_x <= 235):
                        prvni = [209,540]
                        sdilene_polozky.databaze = sdilene_polozky.data10
                        #236-285 =4
                elif (poloha_x >= 236) and (poloha_x <= 285):
                        prvni = [259,540]
                        sdilene_polozky.databaze = sdilene_polozky.data9
                        #286-335 =5
                elif (poloha_x >= 286) and (poloha_x <=335):
                        prvni = [309,540]
                        sdilene_polozky.databaze = sdilene_polozky.data8
                        #336-383 =6
                elif (poloha_x >= 336) and (poloha_x <= 383):
                        prvni = [359,540]
                        sdilene_polozky.databaze = sdilene_polozky.data7
                        #417-467 =7
                elif (poloha_x >= 417) and (poloha_x <= 467):
                        prvni = [443,540]
                        sdilene_polozky.databaze = sdilene_polozky.data6
                        #468-517 =8
                elif (poloha_x >= 468) and (poloha_x <= 517):
                        prvni = [493,540]
                        sdilene_polozky.databaze = sdilene_polozky.data5
                        #518-567 =9
                elif (poloha_x >= 518) and (poloha_x <= 567):
                        prvni = [543,540]
                        sdilene_polozky.databaze = sdilene_polozky.data4
                        #568-617 =10
                elif (poloha_x >= 568) and (poloha_x <= 617):
                        prvni = [593,540]
                        sdilene_polozky.databaze = sdilene_polozky.data3
                        #618-667 =11
                elif (poloha_x >= 618) and (poloha_x <= 667):
                        prvni = [643,540]
                        sdilene_polozky.databaze = sdilene_polozky.data2
                        #668-717 =12
                elif (poloha_x >= 668) and (poloha_x <= 717):
                        prvni = [693,540]
                        sdilene_polozky.databaze = sdilene_polozky.data1
        return prvni

