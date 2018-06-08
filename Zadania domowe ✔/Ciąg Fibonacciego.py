ilosc = int(input('Podaj ilosc liczb do wyswietlenia: '))
a = 0
b = 1
licz = 0


if ilosc <= 0:
   print("Wpisz dodatnia liczbe")
elif ilosc == 1:
   print("Ciag fibonacciego do",ilosc,":")
   print(a)
else:
   print("Ciag fibonacciego do",ilosc,":")
   while licz < ilosc:
       print(a,end=' , ')
       c = a + b
       
       a = b
       b = c
       licz += 1
