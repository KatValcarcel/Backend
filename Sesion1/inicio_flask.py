from flask import Flask

app = Flask(__name__)

# decorador


@app.route('/')
def inicio():
    return 'Bienvenido a mi API'
    # pass


@app.route('/home')
def home():
    # solo retorna string tuplas y diccionarios
    return 'Bienvenido a home'


# app.run()
# modo depuración
if __name__ == '__main__':
    app.run(debug=True)
