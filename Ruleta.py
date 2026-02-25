import random, time

lista1 = ['Manzana','Cereza','Uva','Limon','7']
lista2 = ['Manzana','Cereza','Uva','Limon','7']
lista3 = ['Manzana','Cereza','Uva','Limon','7']

lista1choice =  random.choice(lista1)
lista2choice =  random.choice(lista2)
lista3choice =  random.choice(lista3)
inicio = time.time()

while lista1choice != lista2choice or lista1choice != lista3choice or lista2choice != lista3choice:
    print(lista1choice,lista2choice,lista3choice)
    print('Perdiste\n')
    lista1choice =  random.choice(lista1)
    lista2choice =  random.choice(lista2)
    lista3choice =  random.choice(lista3)
    time.sleep(0.5)

fin = time.time()
diferencia = int(fin - inicio)
print(lista1choice,lista2choice,lista3choice)
print(f'Ganaste, te demoraste {diferencia} segundos en ganar')