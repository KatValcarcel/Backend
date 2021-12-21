from logging import NullHandler
from flask import Flask, request

app = Flask(__name__)

# decorador
# endpoint

# solo con método POST y GET


@app.route('/', methods=['POST', 'GET'])
def inicio():
    print(request.method)
    if request.method == 'POST':
        # request.get_json() => captura el JSON y lo convierte a dictionary
        print(request.get_json())
        data = request.get_json()
        # get llave del dictionary
        if (data.get('nombre')):
            return 'Hola, {}!'.format(data['nombre'])
        else:
            return 'Necesito la información', 400

    elif request.method == 'GET':
        # el primero es la data enviada y el segundo el status http 200: OK
        return 'Bienvenido a mi API de productos', 200


mis_productos = [{
    "nombre": "Paneton con harto bromato",
    "precio": 17.50,
    "disponible": True,
    "fecha_vencimiento": "2022-01-14"
}, {
    "nombre": "Chocolate con harta azucar",
    "precio": 6.90,
    "disponible": False,
    "fecha_vencimiento": "2021-12-30"
}]


@app.route('/productos', methods=['POST', 'GET'])
def productos():
    if request.method == 'GET':
        return{
            'data': mis_productos,
            'message': 'Los productos son',
            'ok': True
            # 'error':'Error al acceder a la BD'
        }
    elif request.method == 'POST':
        data = request.get_json()
        mis_productos.append(data)
        return{
            'data': data,
            'message': 'Producto agregado exitosamente',
            'ok': True
        }, 201


# si no es el tipo de dato, sale 404
@app.route('/producto/<int:id>', methods=['GET', 'POST'])
def producto(id):
    if request.method == 'GET':
        # return{'id': id}
        if len(mis_productos) > id:
            return{
                'data': mis_productos[id],
                'message': 'El producto es',
                'ok': False
            }
        else:
            return{
                'data': 'null',
                'message': 'El producto no existe',
                'ok': False
            }
    # elif request.method == 'POST':


if __name__ == '__main__':
    app.run(debug=True)
