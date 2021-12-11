#variable numérica
numero = 10
numero2 = 10.5

#variable de texto
nombre = "Kat"
html='''<html>
<p>
</p>'''
print('Hola! :)')
print(type(nombre))
soltero=False
print(type(soltero))

#arrays
arreglo=[10,12,40,'Eduardo',14.5,False,[1,2]]

#Diccionario | JSON
curso={
'nombre':'Backend',
'dificultad':'dificil',
}
print(curso['dificultad'])

personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]


# nacionalidad de la primera persona
print(personas[0]['nacionalidad'])
# los hobbies de la segunda persona
print(personas[1]['hobbies'])

# la experiencia del segundo hobbie de la primera persona
print(personas[0]['hobbies'][1]['experiencia'])


# forma de eliminar variables o su contenido si es que es una lista, diccionario u otro 
del personas
# print(personas)