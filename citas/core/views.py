# vistas usando servicio REST
from rest_framework.generics import CreateAPIView

# hereda de CreateAPIView


class PersonasController(CreateAPIView):
    def post(self):
        '''Se ejecutará todo lo relacionado con el método POST de este controlador'''
        return 'Hola amigos'
