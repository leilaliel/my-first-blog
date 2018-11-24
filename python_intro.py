#fonction pour nom
def hi(name):
    if name == 'Lou':
        print('Hi Lou !')
    elif name == 'Solène':
        print('Hi Solène !')
    else:
        print('Hi anonymous person !')

hi('Lou')

hi('Solène')

hi('Jean')

#PLus simple pour nimporte quel nom
def hi(name):
    print('Hi ' + name + '!')

hi('Clothilde')

#boucles
girls = ['Lou', 'Solène', 'Clothilde', 'Zouleikha', 'Leila' ]

for name in girls:
    def hi(name):
        print('Hi ' + name + '!')

for name in girls:
    hi(name)
    print('Next girl')

#boucle avec des nombres
for i in range(1, 6):
    print(i)
#ATTENTION ici, il donne que de 1 à 5
#le range est à moitié ouvert donc le 6 n'est pas inclus
