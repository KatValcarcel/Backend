# vistas usando servicio REST
from rest_framework.generics import CreateAPIView
from .serializers import PersonasSerializer
from rest_framework.response import Response

# hereda de CreateAPIView
class PersonasController(CreateAPIView):
    serializer_class=PersonasSerializer
    def post(self, request):
        print(request)
        '''Se ejecutará todo lo relacionado con el método POST de este controlador'''
        return Response(data='Hola amigos')
