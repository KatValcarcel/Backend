from distutils.command.upload import upload
from tkinter.tix import COLUMN
from django import db
from django.db import models

# Create your models here.


class PersonaModel(models.Model):
    personaId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )
    personaNombre = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='nombre'
    )
    personaApellido = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='apellido'
    )
    personaEmail = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        db_column='email'
    )
    personaFechaNac = models.DateField(
        db_column='fec_nac'
    )
    # Una tupla sirve para agrupar, como si fueran un único valor, varios valores que, por su naturaleza, deben ir juntos.
    opcionesEstadoCivil = [
        # (en el back, en la bd),
        ('SOLTERO', 'SOLTERO'),
        ('CASADO', 'CASADO'),
        ('VIUDO', 'VIUDO'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('COMPLICADO', 'COMPLICADO'),
        ('NO_ESPECIFICA', 'NO_ESPECIFICA')
    ]
    personaEstadoCivil = models.CharField(
        choices=opcionesEstadoCivil,
        db_column='estado_civil',
        default='NO_ESPECIFICA',
        max_length=50
    )
    # imageField guarda la ubicacion, el archivo es guardado dentro del proyecto
    personaFoto = models.ImageField(
        db_column='foto',
        upload_to='personas/',  # almacenamiento dentro del proyecto
        null=True
    )

    # se puede crear una clase dentro de otra clase
    # clase meta sirve para pasar metadata al padre
    # https://docs.djangoproject.com/en/4.0/ref/models/options/
    class Meta:
        # si no se coloca, coloca el nombre del modelo
        db_table = 'personas'
        # para crear una clausula no repetible entre dos o más columnas
        # unique_together = ['nombre', 'apellido', 'estado_civil']


class CitasModel(models.Model):
    citaId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )
    citaDescripcion = models.TextField(
        null=False,
        db_column='descripcion'
    )
    citaFecha = models.DateTimeField(
        db_column='fecha',
        null=False
    )
    citaLatitud = models.FloatField(
        db_column='latitud',
        null=False
    )
    citaLongitud = models.FloatField(
        db_column='longitud',
        null=False
    )
    opcionesEstadoCita = [
        ('ACTIVA', 'ACTIVA'),
        ('CANCELADA', 'CANCELADA'),
        ('POSTPUESTA', 'POSTPUESTA')
    ]
    citaEstado = models.CharField(
        choices=opcionesEstadoCita,
        db_column='estado',
        null=False,
        max_length=50
    )

    createdAt = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at'
    )

    updatedAt = models.DateTimeField(
        auto_now=True,
        db_column='updated_at'
    )
# relaciones
    citador = models.ForeignKey(
        to=PersonaModel,
        db_column='citador_id',
        on_delete=models.PROTECT,
        related_name='personaCitas'
    )
    citado = models.ForeignKey(
        to=PersonaModel,
        db_column='citado_id',
        on_delete=models.PROTECT,
        related_name='personaCitadas'
    )

    class Meta:
        # la tabla se llame citas
        db_table = 'citas'
        # la fecha debe de ser unica con el citador
        # la fecha debe de ser unica con el citado
        # no se indica el nombre de la columna de la base de datos, sino que se indica el nombre del atributo de la clase
        unique_together = [['citaFecha', 'citador'], ['citaFecha', 'citado']]
        # ordenamiento sea por la fecha mas proxima (desc)
        ordering = ['-citaFecha']
