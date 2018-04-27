
#dolnaGranica = int(input("Dolny zakres to: "))
#gornaGranica = int(input("Gorny zakres to: "))
def liczbyPierwszze(dGranica, gGranica):
    print("Liczby pierwsze od ",dGranica," do",gGranica,"to:")
    for liczba in range(dGranica,gGranica + 1):
       # prime numbers are greater than 1
       if liczba > 1:
           for i in range(2,liczba):
               if (liczba % i) == 0:
                   break
           else:
               print(liczba)
def main():
    dGranica=int(input('Podaj od jakiej liczby sprawdzac: '))
    gGranica=int(input('Podaj do jakiej liczby sprawdzac: '))

main()
    