import random

lista1 = ['Manzana','Cereza','Uva','Limon','7']
lista2 = ['Manzana','Cereza','Uva','Limon','7']
lista3 = ['Manzana','Cereza','Uva','Limon','7']

lista1choice =  random.choice(lista1)
lista2choice =  random.choice(lista2)
lista3choice =  random.choice(lista3)
print(lista1choice,lista2choice,lista3choice)
if lista1choice == lista2choice == lista3choice:
    print('Ganste!!!')

else:
    print('Perdiste')