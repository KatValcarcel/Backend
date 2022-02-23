# 1. Cuántas personas tienen más de 20 años
# 2. Qué personas son las que tienen más de 20 años (2)

mas_de_20 = 0
menos_de_20 = "Las personas menores de 20 son "

for persona in personas:
    if(persona['edad'] > 20):
        mas_de_20 += 1
    else:
        menos_de_20 += persona['nombre']+' y '

print(f'Hay {mas_de_20} personas con más de 20 años')
print(menos_de_20)
