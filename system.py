import random


class Data:
    def __init__(self, dzien, miesiac, godzina, minuty):
        self.dzien = dzien
        self.misiac = miesiac
        self.godzina = godzina
        self.minuty = minuty


class PrognozaPogody:
    def __init__(self, data, temperatura, cisnienie, wilgotnosc, wiatr, opad_deszczu, opad_sniegu, slonecza, mgla):
        self.ilosc_dni=0
        self.data = []
        self.temperatura = []
        self.wiatr = []
        self.opad_deszczu = []
        self.opad_sniegu = []
        self.slonecza = []
        self.mgla = []
        self.cisnienie = []
        self.wilgotnosc = []
        self.data.append(data)
        self.temperatura.append(temperatura)
        self.wiatr.append(wiatr)  #m/s
        self.opad_deszczu.append(opad_deszczu)
        self.opad_sniegu.append(opad_sniegu)
        self.slonecza.append(slonecza)
        self.mgla.append(mgla)
        self.cisnienie.append(cisnienie) #hPa
        self.wilgotnosc.append(wilgotnosc) #%
    def Dodaj(self, data, temperatura, cisnienie, wilgotnosc, wiatr, opad_deszczu, opad_sniegu, slonecza, mgla):
        self.data.append(data)
        self.temperatura.append(temperatura)
        self.wiatr.append(wiatr)
        self.opad_deszczu.append(opad_deszczu)
        self.opad_sniegu.append(opad_sniegu)
        self.slonecza.append(slonecza)
        self.mgla.append(mgla)
        self.cisnienie.append(cisnienie)
        self.wilgotnosc.append(wilgotnosc)
        self.ilosc_dni+=1

    def CzyBędziePada_Deszcz(self):

        if self.temperatura[self.ilosc_dni]>10:
            if self.opad_deszczu[self.ilosc_dni]:
                if self.wiatr[self.ilosc_dni]<1.5:
                    return True
                else:
                    if self.temperatura[self.ilosc_dni - 1]-self.temperatura[self.ilosc_dni]>0 and self.cisnienie[self.ilosc_dni - 1]-self.cisnienie[self.ilosc_dni]>0:
                        return True
                    else:
                        return False

            else:
                if (self.temperatura[self.ilosc_dni - 1] - self.temperatura[self.ilosc_dni] > 0 and self.cisnienie[self.ilosc_dni - 1] - self.cisnienie[self.ilosc_dni] > 0)or(self.temperatura[self.ilosc_dni - 1] - self.temperatura[self.ilosc_dni] < 0 and self.cisnienie[self.ilosc_dni - 1] - self.cisnienie[self.ilosc_dni] < 0):
                    return True
                else:
                    return False
        elif self.temperatura[self.ilosc_dni]>-10:
            if self.opad_deszczu[self.ilosc_dni]:
                if self.wiatr[self.ilosc_dni] < 1.5:
                    ran=random.randint(0,100)
                    if ran<100*((self.temperatura[self.ilosc_dni] + 10) / 20):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if self.temperatura[self.ilosc_dni - 1] - self.temperatura[self.ilosc_dni] > 0 and self.cisnienie[self.ilosc_dni - 1] - self.cisnienie[self.ilosc_dni] > 0:
                    ran = random.randint(0, 100)
                    if ran < 100 * ((self.temperatura[self.ilosc_dni] + 10) / 20):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
                return False
    def CzyBędziePada_Snieg(self):

        if self.temperatura[self.ilosc_dni]<-10:
            if self.opad_deszczu[self.ilosc_dni]:
                if self.wiatr[self.ilosc_dni]<1.5:
                    return True
                else:
                    if self.temperatura[self.ilosc_dni - 1]-self.temperatura[self.ilosc_dni]>0 and self.cisnienie[self.ilosc_dni - 1]-self.cisnienie[self.ilosc_dni]>0:
                        return True
                    else:
                        return False

            else:
                if (self.temperatura[self.ilosc_dni - 1] - self.temperatura[self.ilosc_dni] > 0 and self.cisnienie[self.ilosc_dni - 1] - self.cisnienie[self.ilosc_dni] > 0)or(self.temperatura[self.ilosc_dni - 1] - self.temperatura[self.ilosc_dni] < 0 and self.cisnienie[self.ilosc_dni - 1] - self.cisnienie[self.ilosc_dni] < 0):
                    return True
                else:
                    return False
        elif self.temperatura[self.ilosc_dni]<10:
            if self.opad_deszczu[self.ilosc_dni]:
                if self.wiatr[self.ilosc_dni] < 1.5:
                    ran=random.randint(0,100)
                    if ran<100*(-(self.temperatura[self.ilosc_dni] - 10) / 20):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if self.temperatura[self.ilosc_dni - 1] - self.temperatura[self.ilosc_dni] > 0 and self.cisnienie[self.ilosc_dni - 1] - self.cisnienie[self.ilosc_dni] > 0:
                    ran = random.randint(0, 100)
                    if ran<100*(-(self.temperatura[self.ilosc_dni] - 10) / 20):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
                return False
    def CzyBedzieMgła(self):
        if self.wiatr[self.ilosc_dni] > 1.5:
            return False
        else:
            if(self.mgla==0):
                if self.temperatura[self.ilosc_dni - 1]-self.temperatura[self.ilosc_dni]>0 and self.wilgotnosc[self.ilosc_dni]>70:
                    return True
                else:
                    return False
            else:
                 if self.slonecza[self.ilosc_dni]==1:
                    return False
                 else:
                    return True
    def CzyBedzieSmog(self):
        if self.CzyBędziePada_Deszcz() or self.opad_deszczu:
            return False
        else:
            if self.wiatr[self.ilosc_dni]>1.5:
                return False
            else:
                if self.wilgotnosc[self.ilosc_dni]<75:
                    return False
                else:
                    if self.temperatura[self.ilosc_dni]>20:
                        return False
                    elif self.temperatura[self.ilosc_dni]<0:
                        ran = random.randint(0, 100)
                        if ran < 100 * ((self.temperatura[self.ilosc_dni]) / 20):
                            return False
                        else:
                            return True
                    else:
                        return True
    def CzySloneczna(self):
        if self.CzyBędziePada_Deszcz() or self.CzyBedzieMgła() or self.CzyBędziePada_Snieg():
            return False
        else:
            if self.cisnienie[self.ilosc_dni - 1]-self.cisnienie[self.ilosc_dni]<0 and self.cisnienie[self.ilosc_dni]>1013:
                return True
            else:
                if self.wiatr[self.ilosc_dni]<1.5 and self.wilgotnosc[self.ilosc_dni]<25:
                    return self.slonecza[self.ilosc_dni]
                else:
                    return False
    def CzyBiometrKorzystny(self):
        if not self.CzySloneczna() and self.CzyBędziePada_Deszcz():
            return False
        else:
            if self.wiatr[self.ilosc_dni]>1.5:
                return False
            else:
                if self.cisnienie[self.ilosc_dni]>1025 and self.cisnienie[self.ilosc_dni]<1000:
                    return False
                else:
                    if(self.wilgotnosc[self.ilosc_dni]>55):
                        return False
                    else:
                        return True







#data, temperatura, cisnienie, wilgotnosc, wiatr, opad_deszczu, opad_sniegu, slonecza, mgla
progonza = PrognozaPogody(Data(21, 1, 12, 60), 5, 999, 60, 0, 0, 0, 0, 0)
progonza.Dodaj(Data(21, 1, 12, 60), 5, 1015, 70, 0, 0, 0, 0, 0)
# print(progonza.CzyBędziePada_Deszcz())
# print(progonza.CzyBędziePada_Snieg())
# print(progonza.CzySloneczna())
# print(progonza.CzyBedzieMgła())
# print(progonza.CzyBedzieSmog())
# print(progonza.CzyBiometrKorzystny())