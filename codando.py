
ano=int(input('Informe um ano para saber se ele é bissexto: '))
if ano%4!=0:
    print('Não é um ano bissexto')
elif ano%4==0 and ano%100==0 and ano%400!=0:
    print('Não é um ano bissexto')
elif ano%4==0 and ano%100!=0:
    print('É um ano  bissexto ')
elif ano%4==0 and ano%100==0 and ano%400==0:
    print('É um ano bissexto')