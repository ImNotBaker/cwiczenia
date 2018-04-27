


dol = int(input('Podaj od jakiej liczby sprawdzac: '))
gora = int(input('Podaj do jakiej liczby sprawdzac: '))



print("Liczby pierwsze od ",dol,"do",gora,"to:")

for liczba in range(dol,gora + 1):
   
   if liczba> 1:
       for i in range(2,liczba):
           if (liczba % i) == 0:
               break
       else:
           print(liczba)
