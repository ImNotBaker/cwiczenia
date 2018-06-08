#Pętelki
for zmienna in range(10, 20, 3):
    print(zmienna, ' - hello')

lista = ['DE', 'PL', 'FR', 'ES']
#petelka po elementach listy
print("=====================")
for zmienna in lista:
    print (zmienna + ' - hello')

print("=====================")
msg = " ala ma kota i dwa psy"
for a in msg.split():
    print(a)
print(msg.split())

print('=======================')
msge = " ala ma kota i dwa psy. tomek ma psa i dwa koty."
print(msge.split('.'))
for a in msge.split('.'):
    print(len(a))
