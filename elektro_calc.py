def leto ():
    per=o/100 # 1% от суммы
    print ("Потреблено по зонам до 100 кВт*ч         день ",round(d/per,2),"  ночь ",round(n/per,2))
    print ("Потреблено до по зонам свыше 100 кВт*ч   день ",round((d-(d/per)),2),"  ночь ",round((n-(n/per)),2))
    dg100=d/per*0.9
    ng100=n/per*0.45
    print ("Оплата за потребление до 100 кВт*ч, грн     ",round(dg100, 2),"     ",round(ng100, 2))
    dg101=(d-(d/per))*1.68
    ng101=(n-(n/per))*0.84
    print ("Оплата за потребление свыше 100 кВт*ч, грн  ",round(dg101, 2),"     ",round(ng101, 2))
    og=dg100+ng100+dg101+ng101
    print ("Итого к оплате, грн.              ",round(og, 2))
    oldg=(o-100)*1.68 + 90
    eco=oldg-og
    print ("При обычном счетчике оплата, грн  ",round(oldg, 2))
    print ("Вы сэкономили в этом месяце, грн  ",round(eco, 2))

def zima ():
    if o <= 3000:
        dg3000=d*0.9
        ng3000=n*0.45
        print ("Оплата за потребление до 3000 кВт*ч, грн     ",round(dg3000, 2),"     ",round(ng3000, 2))
        og3000=dg3000+ng3000
        print ("Итого к оплате, грн.              ",round(og3000, 2))
        oldg=(o-100)*1.68 + 90
        eco=oldg-og3000
        print ("При обычном счетчике оплата, грн  ",round(oldg, 2))
        print ("Вы сэкономили в этом месяце, грн  ",round(eco, 2))
        
    elif o > 3000:
        dg3000=d*0.9
        ng3000=n*0.45
        print ("Оплата за потребление до 3000 кВт*ч, грн     ",round(dg3000, 2),"     ",round(ng3000, 2))
        dg3001=(o-3000)*1.68
        print ("Оплата за потребление свыше 3000 кВт*ч, грн  ",round(dg3001, 2))
        og=dg3000+ng3000+dg3001
        print ("Итого к оплате, грн.              ",round(og, 2))
        oldg=(o-100)*1.68 + 90
        eco=oldg-og
        print ("При обычном счетчике оплата, грн  ",round(oldg, 2))
        print ("Вы сэкономили в этом месяце, грн  ",round(eco, 2))

d1=int (input ("Введите предыдущее показания день\n"))
d2=int(input ("Введите текущие показания день\n"))
n1=int(input ("Введите предыдущее показания ночь\n"))
n2=int(input ("Введите текущие показания ночь\n"))
d=d2-d1 # Разница дневных показаний
n=n2-n1 # Разница ночных показаний
o=d+n   # Сумма разниц дневных и ночных показаний
print ("Потребление по зонам, кВт*ч              день ",d,"  ночь ",n)
print ("Итого потреблено - ",o," кВт*ч")
ws=input ("Расчет делать по зимнему тарифу? y/n \n")
if ws=="n":
    leto ()
elif ws=="y":
    zima ()
    
